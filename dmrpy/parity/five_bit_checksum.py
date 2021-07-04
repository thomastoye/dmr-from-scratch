def calculate_five_bit_checksum(data: int):
    """Calculate 5-bit checksum as defined in ETSI TS 102 361-1 Section B.3.11

    Parameters:
    data: 72 bits (9 octets)"""

    accumulated = (
        sum([(data >> (octetN * 8)) & 0xFF for octetN in reversed(range(0, 9))])
        & 0xFFFF
    )

    return accumulated % 31
