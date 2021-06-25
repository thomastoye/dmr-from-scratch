from dmrpy.pdu.voice_burst import VoiceBurst
from dmrpy.pdu.cach_burst import CachBurst
from dmrpy.layer_1.symbol_stream_to_packets import symbol_stream_to_packets
from dmrpy.fixtures.symbol_stream import (
    EXAMPLE_SYMBOL_STREAM_SHORT,
)

print(
    "\n".join(
        [
            str(start) + '-' + str(end) + ' ' + str(VoiceBurst.create_from_burst_binary(data)) + '  ' + hex(data)
            for (start, end, kind, data) in symbol_stream_to_packets(EXAMPLE_SYMBOL_STREAM_SHORT)
            if kind != "cach"
        ]
    )
)
