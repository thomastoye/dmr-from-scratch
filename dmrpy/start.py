# from dmrpy.pdu.voice_burst import VoiceBurst
# from dmrpy.pdu.cach_burst import CachBurst
# from dmrpy.layer_1.symbol_stream_to_packets import symbol_stream_to_packets
# from dmrpy.fixtures.symbol_stream import (
#     EXAMPLE_SYMBOL_STREAM_SHORT,
# )

from dmrpy.fixtures.fixtures import FIXTURE, FIXTURE_SAMPLE_RATE
from dmrpy.layer_1.audio_to_symbols import audio_stream_to_symbols
import plotext

result = audio_stream_to_symbols(FIXTURE, FIXTURE_SAMPLE_RATE)
plotext.hist(result[0:4800], bins=100)
plotext.show()


# print(
#     "\n".join(
#         [
#             str(VoiceBurst.create_from_burst_binary(data))
#             for (kind, data) in symbol_stream_to_packets(EXAMPLE_SYMBOL_STREAM_SHORT)
#             if kind != "cach"
#         ]
#     )
# )
