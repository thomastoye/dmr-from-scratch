import numpy as np
from dmrpy.pdu.voice_burst import VoiceBurst
from dmrpy.pdu.cach_burst import CachBurst
from dmrpy.layer_1.symbol_stream_to_packets import symbol_stream_to_packets
from dmrpy.layer_1.audio_to_symbols import audio_stream_to_symbols
from dmrpy.fixtures.fixtures import FIXTURE, FIXTURE_SAMPLE_RATE

symbol_stream = np.array(
    [
        symbol["symbol"]
        for symbol in audio_stream_to_symbols(FIXTURE, FIXTURE_SAMPLE_RATE)
    ]
)

print(
    "\n".join(
        [
            str(start_index).zfill(8)
            + "  "
            + str(VoiceBurst.create_from_burst_binary(data))
            for (kind, data, start_index) in symbol_stream_to_packets(symbol_stream)
            if kind != "cach"
        ]
    )
)
