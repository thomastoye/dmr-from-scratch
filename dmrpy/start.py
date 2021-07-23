import numpy as np
from dmrpy.pdu.voice_burst import VoiceBurst
from dmrpy.pdu.cach_burst import CachBurst
from dmrpy.layer_1.symbol_stream_to_packets import (
    Layer1CachBurst,
    symbol_stream_to_packets,
)
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
            str(burst.start_index).zfill(8)
            + "  "
            + str(burst.start_index + burst.symbol_length).zfill(8)
            + " "
            + hex(burst.data)
            + str(
                CachBurst.create_from_burst_binary(burst.data)
                if isinstance(burst, Layer1CachBurst)
                else VoiceBurst.create_from_burst_binary(burst.data)
            )
            for burst in symbol_stream_to_packets(symbol_stream)
        ]
    )
)
