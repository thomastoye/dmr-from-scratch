from dmrpy.pdu.cach_burst import (
    CachBurst,
    deinterleave_cach_burst,
    interleave_cach_burst,
)


def test_create_from_burst_binary():
    burst = CachBurst.create_from_burst_binary(0xB6C163)

    # 1 0 10 011 01111010001010001
    # | | |  |   Payload
    # | | |  FEC
    # | | LCSS
    # | TC
    # AT

    assert burst.has_valid_fec()
    assert burst.payload == 0xF451
    assert burst.at == 1
    assert burst.tc == 0
    assert burst.lcss == 2

    assert burst.raw_deinterleaved() == 0xA6F451
    assert burst.raw_interleaved() == 0xB6C163


def test_interleaving_then_deinterleaving_yields_same_result():
    orig = 11977059
    assert interleave_cach_burst(deinterleave_cach_burst(orig)) == orig


def test_deinterleave_cach_burst():
    assert deinterleave_cach_burst(0xB6C163) == 0xA6F451


def test_interleave_cach_burst():
    assert interleave_cach_burst(0xA0B799) == 0xA6F451
