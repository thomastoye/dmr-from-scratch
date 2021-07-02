from dmrpy.pdu.emb import Emb
from dmrpy.constants import SYNC_PATTERN
from dmrpy.parity.get_syndrome_for_word import get_syndrome_for_word
from dmrpy.parity.hamming_7_4_3 import parity_check_matrix

# ETSI TS 102 361-1 Section ...
class VoiceBurst:
    def __init__(self, vs, emb=None, embedded_signalling=None):
        """
        Parameters:
        vs                  : Vocoder socket bits (216 bits)
        emb                 : Embedded signalling field (16 bits)
        embedded_signalling : Either link control (LC) or reverse channel (RC) information (32 bits)
        """
        self.vs = vs
        self.emb = None if emb is None else Emb.create_from_binary(emb)
        self.embedded_signalling = embedded_signalling

    def __repr__(self):
        return f"VoiceBurst(vs={hex(self.vs)}, emb={hex(self.emb.raw()) if self.emb is not None else None}, embedded_signalling={hex(self.embedded_signalling) if self.embedded_signalling is not None else None})"

    def raw(self):
        return None

    def create_from_burst_binary(data):
        # A voice burst can be:
        #  | Voice (108) |                  Sync (48)                   | Voice (108) |
        #  | Voice (108) | EMB (8) | Embedded signalling (32) | EMB (8) | Voice (108) |

        possible_sync = (data >> 108) & 0xFFFFFFFFFFFF

        emb = None
        embedded_signalling = None

        if (possible_sync == SYNC_PATTERN["BS_VOICE"]) or (
            possible_sync == SYNC_PATTERN["MS_VOICE"]
        ):
            pass
        else:
            embedded_signalling = (possible_sync >> 8) & 0xFFFFFFFF
            emb = ((possible_sync >> 32) & 0xFF00) + (possible_sync & 0xFF)

        vocoder_socket_bits = ((data >> 48) & ((2 ** 108 - 1) << 108)) + (
            data & (2 ** 108 - 1)
        )

        return VoiceBurst(
            vs=vocoder_socket_bits, emb=emb, embedded_signalling=embedded_signalling
        )
