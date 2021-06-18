import numpy as np

# ETSI TS 102 361-1 B.4.1
CACH_BURST_DEINTERLEAVE_TABLE = [0, 2, 3, 4, 6, 7, 8, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22, 1, 5, 9, 11, 15, 19, 23]
CACH_BURST_INTERLEAVE_TABLE = [0, 17, 1, 2, 3, 18, 4, 5, 6, 19, 7, 20, 8, 9, 10, 21, 11, 12, 13, 22, 14, 15, 16, 23]


def interleave_cach_burst(cach_burst, interleave_table=CACH_BURST_INTERLEAVE_TABLE):
    result = 0

    for i in range(23,-1, -1):
        mask = 2 ** (interleave_table[i])
        result = (result << 1) + ((cach_burst & mask) >> (interleave_table[i]))

    return result

def deinterleave_cach_burst(cach_burst):
    return interleave_cach_burst(cach_burst, interleave_table=CACH_BURST_DEINTERLEAVE_TABLE)

# Purpose of CACH (ETSI TS 102 361-1 Section 4.5):
#  1. Indicate the usage of the inbound time slot
#  2. Indicate the channel number of the inbound and outbound time slots
#  3. Carry additional low speed signalling as described in clause 7.1.4
class CachBurst:
    # at      : access (1 bit)               \
    # tc      : numbering (1 bit)            |
    # ls/lcss : framing (2 bits)             |     Known together as "TDMA Access Channel Type" (TACT) bits
    # h       : hamming parity bits (3 bits) /
    # p       : payload (17 bits)            --> Payload NOT protected by Hamming FEC
    def __init__(self, raw, access, numbering, framing, hamming, payload):
        self.raw = raw

        # Interpretation of at and tc (ETSI TS 102 361-1 Section 6.3):
        #  Where DMR activity is present on the outbound channel,
        #  then the AT bit in each CACH shall indicate to MSs whether
        #  the next slot on the inbound channel whose TDMA channel number
        #  is indicated by the TC bit is "Idle" or "Busy"
        # Typically a BS shall set the AT to "Busy" while DMR activity is present on the inbound channel
        self.access = access
        self.numbering = numbering

        # LCSS indicates that this burst contains the beginning, end, or continuation of an LC or CSBK signalling
        # Due to the small number of bits available, there is no single fragment LC signalling defined
        self.framing = framing

        self.hamming = hamming

        self.payload = payload
        self.tact = np.array(
            [
                access,
                numbering,
                (framing & 0x2) >> 1,
                (framing & 0x1),
                (hamming & 0x4) >> 2,
                (hamming & 0x2) >> 1,
                (hamming & 0x1),
            ]
        )

    def __repr__(self):
        return f'CACH burst (FEC { "" if self.has_valid_fec() else "in" }valid): at {self.access}, tc {self.numbering}, ls {hex(self.framing)}, payload {hex(self.payload)} [raw (deinterleaved) {hex(self.raw)}]'

    # Only TACT is protected by FEC
    def has_valid_fec(self):
        return np.array_equal(
            (self.tact @ HAMMING_7_4_3_PARITY_CHECK) % 2, np.array([0, 0, 0])
        )

    def create_from_burst_binary(data):
        deinterleaved = deinterleave_cach_burst(
            [int(i) for i in bin(data)[2:].zfill(24)]
        )

        return CachBurst(
            bit_array_to_decimal(deinterleaved),
            deinterleaved[0],
            deinterleaved[1],
            (deinterleaved[2] << 1) + deinterleaved[3],
            (deinterleaved[4] << 2) + (deinterleaved[5] << 1) + deinterleaved[6],
            bit_array_to_decimal(deinterleaved[7:]),
        )