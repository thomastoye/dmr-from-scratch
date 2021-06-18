from dmrpy.parity.get_syndrome_for_word import get_syndrome_for_word
from dmrpy.parity.hamming_7_4_3 import parity_check_matrix
import numpy as np
from numpy.testing import assert_array_equal

VALID_WORD_1 = [0, 0, 0, 0, 0, 0, 0]
VALID_WORD_2 = [0, 0, 0, 1, 0, 1, 1]
VALID_WORD_3 = [1, 1, 1, 1, 1, 1, 1]
VALID_WORD_4 = [1, 1, 0, 0, 0, 1, 0]

INVALID_WORD_1 = [1, 1, 0, 0, 0, 1, 1]
INVALID_WORD_2 = [0, 0, 0, 0, 1, 1, 1]

CORRECT_SYNDROME = np.array([ 0, 0, 0 ])

def test_hamming_7_4_3_valid_words():
    assert_array_equal(get_syndrome_for_word(VALID_WORD_1, parity_check_matrix), CORRECT_SYNDROME)
    assert_array_equal(get_syndrome_for_word(VALID_WORD_2, parity_check_matrix), CORRECT_SYNDROME)
    assert_array_equal(get_syndrome_for_word(VALID_WORD_3, parity_check_matrix), CORRECT_SYNDROME)
    assert_array_equal(get_syndrome_for_word(VALID_WORD_4, parity_check_matrix), CORRECT_SYNDROME)

def test_hamming_7_4_3_invalid_words():
    assert_array_equal(get_syndrome_for_word(INVALID_WORD_1, parity_check_matrix), np.array([0, 0, 1]))
    assert_array_equal(get_syndrome_for_word(INVALID_WORD_2, parity_check_matrix), np.array([1, 1, 1]))
