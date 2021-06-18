import numpy as np

# See https://en.wikipedia.org/wiki/Parity-check_matrix#Creating_a_parity_check_matrix

def derive_parity_check_matrix_from_generator(generator: np.ndarray):
    k = generator.shape[0]
    n = generator.shape[1]

    return np.concatenate((np.transpose(generator[:,k:]), np.identity(n-k, dtype=int)), axis=1)
