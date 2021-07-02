from dmrpy.util.to_numpy_bit_array import to_numpy_bit_array
from numpy.testing import assert_array_equal


def test_to_numpy_bit_array():
    assert_array_equal(
        to_numpy_bit_array(0x1391, 16), [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1]
    )
