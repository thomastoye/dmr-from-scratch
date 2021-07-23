from dmrpy.pdu.data_burst import DataBurst


def test_create_with_sync():
    burst = DataBurst.create_from_burst_binary(
        0xF338460C8B6859896495E10EA1BDFF57D75DF5DBF16DE363672469F8C83D3AFFE0
    )

    assert burst.info == 0xF338460C8B6859896495E10E96DE363672469F8C83D3AFFE0
    assert burst.embedded_signalling == None
    assert burst.slot_type.raw() == 0x86EFC
    assert burst.slot_type.cc == 8
    assert burst.slot_type.data_type == 6
    assert burst.slot_type.parity == 0xEFC
