from dmrpy.pdu.emb import Emb


def test_emb():
    emb = Emb.create_from_binary(0x1391)
    assert emb.cc == 1
    assert emb.pi == 0
    assert emb.lcss == 1
    assert emb.fec == 0x191
    assert emb.raw() == 0x1391
    assert str(emb) == 'Emb(cc=0x1, pi=0x0, lcss=0x1, fec=0x191)'
