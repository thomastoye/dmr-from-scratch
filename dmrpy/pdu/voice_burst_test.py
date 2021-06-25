from dmrpy.pdu.voice_burst import VoiceBurst

# TODO EMB/embedded signalling decoding for voice superframes
VOICE_SUPERFRAME = [
    VoiceBurst(vs=0xd9291739ca0ec7f59ccc71d270b60c7e56cba1e, emb=None, embedded_signalling=None),
    VoiceBurst(vs=0xf5b1c31affc6246b8e361b2d015b94e85eda12b, emb=0x8, embedded_signalling=0xaca0aca9),
    VoiceBurst(vs=0xd9291739ca0ec7f59ccc6dd270b60c7e56cba1e, emb=0xc, embedded_signalling=0x5fd7df71),
    VoiceBurst(vs=0xfd1c25ae9d8fbe5ae8bae207b1bef221316663, emb=0x8, embedded_signalling=0xa6acb7a6),
    VoiceBurst(vs=0xd9291739ca0ec7f59ccc6dd270b60c7e56cba1e, emb=0xc, embedded_signalling=0x5fd7df71),
    VoiceBurst(vs=0x3d70f248ddabc7dcd56cecdb831f8b1b1921b23, emb=0x7, embedded_signalling=0xafb4bbbb)
]

def test_create_with_sync():
    burst = VoiceBurst.create_from_burst_binary(0xf968f40102cdb76d9291739ca0e755fd7df75f75295c4ecfbdb1e260c7e56cba1e)
    assert burst.emb == None
    assert burst.embedded_signalling == None
    assert burst.vs == 0xf968f40102cdb76d9291739ca0e5295c4ecfbdb1e260c7e56cba1e

def test_create_no_sync():
    burst = VoiceBurst.create_from_burst_binary(0x4f50e8d839116fef5b1c31affc58daca0aca98b96beed8971a16aab94e85eda12b)

    assert burst.embedded_signalling == 0xaca0aca9
    assert burst.emb == 0x8d8b
    assert burst.vs == 0x4f50e8d839116fef5b1c31affc596beed8971a16aab94e85eda12b
