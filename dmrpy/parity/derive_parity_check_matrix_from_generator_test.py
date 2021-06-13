from dmrpy.parity.derive_parity_check_matrix_from_generator import derive_parity_check_matrix_from_generator
import numpy as np
from numpy.testing import assert_array_equal

HAMMING_7_4_3_GENERATOR = np.array([
    [1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1]
])

HAMMING_7_4_3_PARITY_CHECK = np.array([
    [1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1]
]).transpose()

def test_derive_parity_check_matrix_from_generator():
    assert_array_equal(HAMMING_7_4_3_PARITY_CHECK, derive_parity_check_matrix_from_generator(HAMMING_7_4_3_GENERATOR))
