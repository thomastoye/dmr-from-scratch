from dmrpy.parity.derive_parity_check_matrix_from_generator import derive_parity_check_matrix_from_generator
import numpy as np

generator = np.array([
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,0],
    [0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,1],
    [0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,0 ,1],
    [0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1],
    [0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0],
    [0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ,1],
    [0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,1]
])

parity_check_matrix = derive_parity_check_matrix_from_generator(generator)

TODO not quite there... See doi:10.1109/cecnet.2011.5768240 - they get a different parity matrix...

Example valid Golay (20,8) words: 0x54469, 0xde34b, 0xffd6d, 0x293e
