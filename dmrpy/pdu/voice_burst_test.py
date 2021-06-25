from dmrpy.pdu.voice_burst import VoiceBurst

# TODO EMB/embedded signalling decoding for voice superframes
VOICE_SUPERFRAME = [
    VoiceBurst(
        vs=0xF968F40102CDB76D9291739CA0E5295C4ECFBDB1E260C7E56CBA1E,
        emb=None,
        embedded_signalling=None,
    ),
    VoiceBurst(
        vs=0x4F50E8D839116FEF5B1C31AFFC596BEED8971A16AAB94E85EDA12B,
        emb=0x8D8B,
        embedded_signalling=0xACA0ACA9,
    ),
    VoiceBurst(
        vs=0xF968F40102CDB76D9291739CA0E5295C4ECFBDB1E260C7E56CBA1E,
        emb=0x75F7,
        embedded_signalling=0x5FD7DF71,
    ),
    VoiceBurst(
        vs=0x8138AB9E23BB520FD1C25AE9D86E3F01D407950CEBEF221316663,
        emb=0x8D8B,
        embedded_signalling=0xA6ACB7A6,
    ),
    VoiceBurst(
        vs=0xF968F40102CDB76D9291739CA0E5295C4ECFBDB1E260C7E56CBA1E,
        emb=0x75F7,
        embedded_signalling=0x5FD7DF71,
    ),
    VoiceBurst(
        vs=0x2A46ED983DAA4DF3D70F248DDAB382D20B130E34AFF8B1B1921B23,
        emb=0x8FF8,
        embedded_signalling=0xAFB4BBBB,
    ),
]


def test_create_with_sync():
    burst = VoiceBurst.create_from_burst_binary(
        0xF968F40102CDB76D9291739CA0E755FD7DF75F75295C4ECFBDB1E260C7E56CBA1E
    )
    assert burst.emb == None
    assert burst.embedded_signalling == None
    assert burst.vs == 0xF968F40102CDB76D9291739CA0E5295C4ECFBDB1E260C7E56CBA1E


def test_create_no_sync():
    burst = VoiceBurst.create_from_burst_binary(
        0x4F50E8D839116FEF5B1C31AFFC58DACA0ACA98B96BEED8971A16AAB94E85EDA12B
    )

    assert burst.embedded_signalling == 0xACA0ACA9
    assert burst.emb == 0x8D8B
    assert burst.vs == 0x4F50E8D839116FEF5B1C31AFFC596BEED8971A16AAB94E85EDA12B
