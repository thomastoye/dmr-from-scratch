from dmrpy.parity.get_syndrome_for_word import get_syndrome_for_word
from dmrpy.parity.quadratic_residue_16_7_6 import parity_check_matrix
import numpy as np
from numpy.testing import assert_array_equal

VALID_WORD_1 = [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1]

CORRECT_SYNDROME = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])


def test_quadratic_residue_16_7_6_valid_word():
    assert_array_equal(
        get_syndrome_for_word(VALID_WORD_1, parity_check_matrix), CORRECT_SYNDROME
    )
