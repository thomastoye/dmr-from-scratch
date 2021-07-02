from dmrpy.pdu.voice_burst import VoiceBurst

VOICE_SUPERFRAME = [
    # Data head (7.1.1): 0x2B6004101F842DD00DF07D41046DFF57D75DF5DE30152E2070B20F803F88C695E2
    # See 7.1.3: A: Sync, B-E: Link Control, F: Reverse Channel Opportunity
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6BB9E881526755FD7DF75F7173002A6BB9E881526173002A6A
    ),  # A
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6BB9E881526134E0F060691173002A6BB9E881526173002A6A
    ),  # B
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6BB9E881526171711004774173002A6BB9E881526173002A6A
    ),  # C
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6B954BE6500170C03181B74310B00777A6C6CB53732789483A
    ),  # D
    VoiceBurst.create_from_burst_binary(
        0x865AE7617555B50601B758E665115175A0F4E07124815001FFF5A337706128A7CA
    ),  # E
    VoiceBurst.create_from_burst_binary(
        0xEEE7817574614DF2FFCCF4A05511100000000E243059E7F9E908A0756202CCD622
    ),  # F
    # Voice term (7.1.2): 0x2B0F04C41F342DA80D807DE104ADFF57D75DF5D965012D1877D203C03788DF95D1
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
    assert burst.emb.raw() == 0x8D8B
    assert burst.vs == 0x4F50E8D839116FEF5B1C31AFFC596BEED8971A16AAB94E85EDA12B


def test_voice_superframe():
    assert VOICE_SUPERFRAME[0].emb == None
    assert VOICE_SUPERFRAME[1].emb is not None
    assert VOICE_SUPERFRAME[2].emb is not None
    assert VOICE_SUPERFRAME[3].emb is not None
    assert VOICE_SUPERFRAME[4].emb is not None
    assert VOICE_SUPERFRAME[5].emb is not None
