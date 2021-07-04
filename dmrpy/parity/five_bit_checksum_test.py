from dmrpy.parity.five_bit_checksum import calculate_five_bit_checksum


def test_calculate_five_bit_checksum():
    assert calculate_five_bit_checksum(0x1020000C302F9BE5) == 0xC
