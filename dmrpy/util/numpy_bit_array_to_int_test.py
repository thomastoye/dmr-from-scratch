from dmrpy.util.numpy_bit_array_to_int import numpy_bit_array_to_int


def test_numpy_bit_array_to_int():
    assert numpy_bit_array_to_int(
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1]
    ), 0x1391
