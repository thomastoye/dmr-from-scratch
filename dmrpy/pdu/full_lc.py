from dmrpy.util.numpy_bit_array_to_int import numpy_bit_array_to_int
from dmrpy.util.to_numpy_bit_array import to_numpy_bit_array
import numpy as np
from dmrpy.pdu.voice_burst import VoiceBurst
from dmrpy.parity.five_bit_checksum import calculate_five_bit_checksum
from typing import List


class FullLC:
    def __init__(self, pf, reserved, flco, fid, data, cs_5bit=None):
        """See ETSI TS 102 361-1 Section 9.1.6

        Parameters:
        pf: Protect Flag (1 bit)
        reserved: Reserved (1 bit)
        flco: Full Link Control Opcode (6 bits)
        fid: Feature Set ID (8 bits)
        data: Full LC data (56 bits)
        crc: Full LC CRC, either Reed-Solomon (12,9) FEC or a 5 bit checksum
        """

        self.pf = pf
        self.reserved = reserved
        self.flco = flco
        self.fid = fid
        self.data = data
        self.cs_5bit = cs_5bit

    def raw(self):
        """Create binary representation (without checksum)"""
        return (
            (self.pf << 71)
            + (self.reserved << 70)
            + (self.flco << 64)
            + (self.fid << 56)
            + self.data
        )

    def create_from_embedded_signalling_binary(binary: int, checksum: int):
        # 77 bits
        return FullLC(
            pf=(binary >> 71) & 0x1,
            reserved=(binary >> 70) & 0x1,
            flco=(binary >> 64) & 0x3F,
            fid=(binary >> 56) & 0xFF,
            data=binary & 0xFFFFFFFFFFFFFF,
            cs_5bit=checksum,
        )

    def create_from_superframe(superframe: List[VoiceBurst]):
        assert len(superframe) == 6
        assert superframe[0].embedded_signalling == None  # Should be SYNC

        # See ETSI TS 102 361-1 Section 7.1.3.1
        # Voice superframe example:
        # A: (Sync)
        # B:  lcss=0x1 - 0x4e0f0606
        # C:  lcss=0x3 - 0x17110047
        # D:  lcss=0x3 - 0x0c03181b
        # E:  lcss=0x2 - 0x175a0f4e
        # F: (lcss=0x0 - 0x00000000)

        # Embedded signallings for frames B-E
        embedded_signallings = [frame.embedded_signalling for frame in superframe[1:5]]

        # Perform deinterleaving, see B.2.1
        # We have 4 embedded bursts => N=8 => 7*LC info + 1*simple parity check
        # The BPTC encoding matrix has 8 rows, 16 columns (= 128 bits)
        # The transmit matrix has      4 rows, 32 columns (= 128 bits)

        transmit_matrix = np.array(
            [to_numpy_bit_array(x, 32) for x in embedded_signallings]
        )
        bptc_encode_matrix = transmit_matrix.reshape(16, 8).transpose()

        lc = np.concatenate(
            (
                bptc_encode_matrix[0][0:11],
                bptc_encode_matrix[1][0:11],
                bptc_encode_matrix[2][0:10],
                bptc_encode_matrix[3][0:10],
                bptc_encode_matrix[4][0:10],
                bptc_encode_matrix[5][0:10],
                bptc_encode_matrix[6][0:10],
            )
        )

        checksum_bits = np.array(
            [
                bptc_encode_matrix[2][10],
                bptc_encode_matrix[3][10],
                bptc_encode_matrix[4][10],
                bptc_encode_matrix[5][10],
                bptc_encode_matrix[6][10],
            ]
        )

        return FullLC.create_from_embedded_signalling_binary(
            numpy_bit_array_to_int(lc), numpy_bit_array_to_int(checksum_bits)
        )

    def checksum_matches(self):
        # TODO handle case where checksum is not 5-bit checksum
        return calculate_five_bit_checksum(self.raw()) == self.cs_5bit

    def create_from_header_or_terminator_burst_binary(binary):
        # 96 bits - TODO
        pass

    def create_from_bptr_transmit_matrix(matrix):
        pass
