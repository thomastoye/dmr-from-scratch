from dmrpy.parity.derive_parity_check_matrix_from_generator import (
    derive_parity_check_matrix_from_generator,
)
import numpy as np
from numpy.testing import assert_array_equal

HAMMING_7_4_3_GENERATOR = np.array(
    [
        [1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1],
    ]
)

HAMMING_7_4_3_PARITY_CHECK = np.array(
    [[1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]]
)

GOLAY_20_8_GENERATOR = np.array(
    [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    ]
)

# Ref doi:10.1109/cecnet.2011.5768240
GOLAY_20_8_PARITY_CHECK = np.array(
    [
        [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]
).transpose()


def test_derive_parity_check_matrix_from_generator_hamming():
    assert_array_equal(
        HAMMING_7_4_3_PARITY_CHECK,
        derive_parity_check_matrix_from_generator(HAMMING_7_4_3_GENERATOR),
    )


def test_derive_parity_check_matrix_from_generator_golay():
    assert_array_equal(
        GOLAY_20_8_PARITY_CHECK,
        derive_parity_check_matrix_from_generator(GOLAY_20_8_GENERATOR),
    )
