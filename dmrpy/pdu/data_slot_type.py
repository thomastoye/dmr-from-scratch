class DataSlotTypePdu:
    """
    ETSI TS 102 361-1 Section 6.2; Section 9.1.3
    Parity: Golay (20,8) FEC
    """

    def __init__(self, cc: int, data_type: int, parity: int) -> None:
        self.cc = cc
        self.data_type = data_type
        self.parity = parity
        pass

    def create_from_binary(data: int):
        cc = (data >> 16) & 0x4
        data_type = (data >> 12) & 0x4
        parity = data & 0xFFF

        return DataSlotTypePdu(cc, data_type, parity)
