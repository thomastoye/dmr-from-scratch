from dmrpy.pdu.cach_burst import CachBurst, deinterleave_cach_burst, interleave_cach_burst

# def test_1():
#     burst = CachBurst.create_from_burst_binary(11977059)
#     assert burst.has_valid_fec()

def test_interleaving_then_deinterleaving_yields_same_result():
    orig = 11977059
    assert interleave_cach_burst(deinterleave_cach_burst(orig)) == orig

def test_deinterleave_cach_burst():
    assert deinterleave_cach_burst(0xb6c163) == 0xa6f451

def test_interleave_cach_burst():
    assert interleave_cach_burst(0xa0b799) == 0xa6f451
