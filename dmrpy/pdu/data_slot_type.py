from dmrpy.parity.get_syndrome_for_word import get_syndrome_for_word
from dmrpy.parity.golay_20_8_7 import parity_check_matrix
import numpy as np
from dmrpy.util.to_numpy_bit_array import to_numpy_bit_array
from enum import IntEnum

# ETSI TS 102 361-1 Section 9.3.6
class DataType(IntEnum):
    PI_HEADER = 0
    VOICE_LC_HEADER = 1
    TERMINATOR_WITH_LC = 2
    CSBK = 3
    MBC_HEADER = 4
    MBC_CONTINUATION = 5
    DATA_HEADER = 6
    RATE_1_2_DATA = 7
    RATE_3_4_DATA = 8
    IDLE = 9
    RATE_1_DATA = 10
    UNIFIED_SINGLE_BLOCK_DATA = 11
    RESERVED_1100 = 12
    RESERVED_1101 = 13
    RESERVED_1110 = 14
    RESERVED_1111 = 15


class DataSlotTypePdu:
    """
    ETSI TS 102 361-1 Section 6.2; Section 9.1.3
    Parity: Golay (20,8) FEC
    """

    def __init__(self, cc: int, data_type: int, parity: int) -> None:
        self.cc = cc
        self.data_type = data_type
        self.parity = parity

    def __repr__(self):
        return f"DataSlotTypePdu(cc={self.cc}, data_type={self.data_type}, parity={hex(self.parity)})"

    def raw(self):
        return (self.cc << 16) + (self.data_type << 12) + (self.parity)

    def has_valid_fec(self):
        word = to_numpy_bit_array(self.raw(), 20)
        return np.array_equal(
            get_syndrome_for_word(word, parity_check_matrix),
            np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        )

    def create_from_binary(data: int):
        cc = (data >> 16) & 0xF
        data_type = (data >> 12) & 0xF
        parity = data & 0xFFF

        return DataSlotTypePdu(cc, data_type, parity)
