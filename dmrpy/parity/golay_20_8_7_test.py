from dmrpy.parity.get_syndrome_for_word import get_syndrome_for_word
from dmrpy.parity.golay_20_8_7 import parity_check_matrix
import numpy as np
from numpy.testing import assert_array_equal

VALID_WORD_1 = [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]  # 0x54469
VALID_WORD_2 = [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1]  # 0xde34b
VALID_WORD_3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1]  # 0xffd6d
VALID_WORD_4 = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0]  # 0x0293e

INVALID_WORD_1 = [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
INVALID_WORD_2 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]

CORRECT_SYNDROME = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def test_golay_20_8_valid_words():
    assert_array_equal(
        get_syndrome_for_word(VALID_WORD_1, parity_check_matrix), CORRECT_SYNDROME
    )
    assert_array_equal(
        get_syndrome_for_word(VALID_WORD_2, parity_check_matrix), CORRECT_SYNDROME
    )
    assert_array_equal(
        get_syndrome_for_word(VALID_WORD_3, parity_check_matrix), CORRECT_SYNDROME
    )
    assert_array_equal(
        get_syndrome_for_word(VALID_WORD_4, parity_check_matrix), CORRECT_SYNDROME
    )


def test_golay_20_8_invalid_words():
    assert_array_equal(
        get_syndrome_for_word(INVALID_WORD_1, parity_check_matrix),
        np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1]),
    )
    assert_array_equal(
        get_syndrome_for_word(INVALID_WORD_2, parity_check_matrix),
        np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]),
    )
