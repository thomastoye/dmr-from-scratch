from dmrpy.pdu.voice_burst import VoiceBurst
from dmrpy.pdu.cach_burst import CachBurst
from dmrpy.layer_1.symbol_stream_to_packets import symbol_stream_to_packets
from dmrpy.fixtures.symbol_stream import (
    EXAMPLE_SYMBOL_STREAM_SHORT,
)

print(
    "\n".join(
        [
            str(VoiceBurst.create_from_burst_binary(data))
            for (kind, data) in symbol_stream_to_packets(EXAMPLE_SYMBOL_STREAM_SHORT)
            if kind != "cach"
        ]
    )
)
