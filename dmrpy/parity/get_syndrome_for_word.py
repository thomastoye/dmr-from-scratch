def get_syndrome_for_word(codeword, parity_check_matrix):
    return (codeword @ parity_check_matrix.transpose()) % 2
