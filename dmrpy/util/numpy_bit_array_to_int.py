def numpy_bit_array_to_int(l):
    return sum([bit << (len(l) - idx) for (idx, bit) in enumerate(l)])
