from dmrpy.pdu.emb import Emb


def test_emb():
    emb = Emb.create_from_binary(0x1391)
    assert emb.cc == 1
    assert emb.pi == 0
    assert emb.lcss == 1
    assert emb.fec == 0x191
    assert emb.raw() == 0x1391
