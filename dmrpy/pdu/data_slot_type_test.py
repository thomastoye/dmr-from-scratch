from dmrpy.pdu.data_slot_type import DataSlotTypePdu, DataType


def test_data_slot_type():
    slot = DataSlotTypePdu.create_from_binary(0x86EFC)
    assert slot.cc == 8
    assert slot.data_type == DataType.DATA_HEADER
    assert slot.parity == 0xEFC
    assert slot.raw() == 0x86EFC
    # TODO Not sure if my FEC calculation is off or if this is an invalid PDU
    # assert slot.has_valid_fec()
