from dmrpy.parity.get_syndrome_for_word import get_syndrome_for_word
from dmrpy.parity.hamming_7_4_3 import parity_check_matrix
import numpy as np

# ETSI TS 102 361-1 B.4.1
CACH_BURST_DEINTERLEAVE_TABLE = [
    0,
    2,
    3,
    4,
    6,
    7,
    8,
    10,
    12,
    13,
    14,
    16,
    17,
    18,
    20,
    21,
    22,
    1,
    5,
    9,
    11,
    15,
    19,
    23,
]

# ETSI TS 102 361-1 B.4.1
CACH_BURST_INTERLEAVE_TABLE = [
    0,
    17,
    1,
    2,
    3,
    18,
    4,
    5,
    6,
    19,
    7,
    20,
    8,
    9,
    10,
    21,
    11,
    12,
    13,
    22,
    14,
    15,
    16,
    23,
]


def interleave_cach_burst(cach_burst, interleave_table=CACH_BURST_INTERLEAVE_TABLE):
    result = 0

    for i in range(23, -1, -1):
        mask = 2 ** (interleave_table[i])
        result = (result << 1) + ((cach_burst & mask) >> (interleave_table[i]))

    return result


def deinterleave_cach_burst(cach_burst):
    return interleave_cach_burst(
        cach_burst, interleave_table=CACH_BURST_DEINTERLEAVE_TABLE
    )


# Purpose of CACH (ETSI TS 102 361-1 Section 4.5):
#  1. Indicate the usage of the inbound time slot
#  2. Indicate the channel number of the inbound and outbound time slots
#  3. Carry additional low speed signalling as described in clause 7.1.4
class CachBurst:
    # at      : access (1 bit)               \
    # tc      : numbering (1 bit)            |
    # ls/lcss : framing (2 bits)             |     Known together as "TDMA Access Channel Type" (TACT) bits
    # fec     : hamming parity bits (3 bits) /
    # payload : payload (17 bits)            --> Payload NOT protected by Hamming FEC
    def __init__(self, at, tc, lcss, payload, fec=None):
        # TODO if FEC is None, calculate FEC

        # Interpretation of at and tc (ETSI TS 102 361-1 Section 6.3):
        #  Where DMR activity is present on the outbound channel,
        #  then the AT bit in each CACH shall indicate to MSs whether
        #  the next slot on the inbound channel whose TDMA channel number
        #  is indicated by the TC bit is "Idle" or "Busy"
        # Typically a BS shall set the AT to "Busy" while DMR activity is present on the inbound channel
        self.at = at
        self.tc = tc

        # LCSS indicates that this burst contains the beginning, end, or continuation of an LC or CSBK signalling
        # Due to the small number of bits available, there is no single fragment LC signalling defined
        # 
        # ETSI TS 102 361-1 Section 9.3.3:
        #   0: Either single fragment LC or first fragment of CSBK signalling
        #      (There is no Single fragment LC defined for CACH signalling.)
        #   1: First fragment of LC signalling
        #   2: Last fragment of LC or CSBK signalling
        #   3: Continuation fragment of LC or CSBK signalling
        self.lcss = lcss

        self.fec = fec

        self.payload = payload
        self.tact = np.array(
            [
                at,
                tc,
                (lcss & 0x2) >> 1,
                (lcss & 0x1),
                (fec & 0x4) >> 2,
                (fec & 0x2) >> 1,
                (fec & 0x1),
            ]
        )

    def __repr__(self):
        return f"CachBurst(at={self.at}, tc={self.tc}, lcss={self.lcss}, fec={self.fec}, payload={hex(self.payload)})"

    def raw_deinterleaved(self):
        return (
            (self.at << 23)
            + (self.tc << 22)
            + (self.lcss << 20)
            + (self.fec << 17)
            + self.payload
        )

    def raw_interleaved(self):
        return interleave_cach_burst(self.raw_deinterleaved())

    # Only TACT is protected by FEC
    def has_valid_fec(self):
        return np.array_equal(
            get_syndrome_for_word(self.tact, parity_check_matrix), np.array([0, 0, 0])
        )

    def create_from_burst_binary(data):
        deinterleaved = deinterleave_cach_burst(data)

        return CachBurst(
            at=(deinterleaved >> 23) & 0x1,
            tc=(deinterleaved >> 22) & 0x1,
            lcss=(deinterleaved >> 20) & 0x3,
            fec=(deinterleaved >> 17) & 0x7,
            payload=deinterleaved & ((2 ** 17) - 1),
        )
