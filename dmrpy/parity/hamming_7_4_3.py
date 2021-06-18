from dmrpy.parity.derive_parity_check_matrix_from_generator import (
    derive_parity_check_matrix_from_generator,
)
import numpy as np

generator = np.array(
    [
        [1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1],
    ]
)

parity_check_matrix = derive_parity_check_matrix_from_generator(generator)
