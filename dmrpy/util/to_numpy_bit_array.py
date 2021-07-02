import numpy as np


def to_numpy_bit_array(n, length):
    """Returns a numpy array of 1s and 0s for a given number"""

    return np.array([int(x) for x in bin(n)[2:].zfill(length)])
