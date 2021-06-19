from dmrpy.pdu.cach_burst import (
    CachBurst,
    deinterleave_cach_burst,
    interleave_cach_burst,
)


def test_create_from_burst_binary():
    burst = CachBurst.create_from_burst_binary(0xb6c163)

    # 1 0 10 011 01111010001010001
    # | | |  |   Payload
    # | | |  FEC
    # | | LCSS
    # | TC
    # AT

    assert burst.has_valid_fec()
    assert burst.payload == 0xf451
    assert burst.access == 1
    assert burst.numbering == 0
    assert burst.framing == 2


def test_interleaving_then_deinterleaving_yields_same_result():
    orig = 11977059
    assert interleave_cach_burst(deinterleave_cach_burst(orig)) == orig


def test_deinterleave_cach_burst():
    assert deinterleave_cach_burst(0xB6C163) == 0xA6F451


def test_interleave_cach_burst():
    assert interleave_cach_burst(0xA0B799) == 0xA6F451
