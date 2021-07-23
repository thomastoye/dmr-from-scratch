from dmrpy.pdu.data_slot_type import DataSlotTypePdu
from dmrpy.constants import SYNC_PATTERN

# ETSI TS 102 361-1 Section 6.2
class DataBurst:
    def __init__(self, info, slot_type, embedded_signalling=None):
        """
        Parameters:
        info                : Data bits (196 bits)
        slot_type           : Slot type (20 bits)
        embedded_signalling : Embedded signalling (or None for data sync) (48 bits)
        """
        self.info = info
        self.slot_type = DataSlotTypePdu.create_from_binary(slot_type)
        self.embedded_signalling = embedded_signalling

    def __repr__(self):
        return f"DataBurst(info={hex(self.info)}, slot_type={str(self.slot_type)}, embedded_signalling={hex(self.embedded_signalling) if self.embedded_signalling is not None else None})"

    def raw(self):
        pass

    def create_from_burst_binary(data):
        # Structure of a data burst:
        #  | Info (98) | Slot type (10) | Embedded signalling / Sync (48) | Slot type (10) | Info (98) |

        possible_sync = (data >> 108) & 0xFFFFFFFFFFFF
        slot_type = ((data >> 146) & (0x3FF << 10)) + ((data >> 98) & 0x3FF)

        embedded_signalling = None

        if (possible_sync != SYNC_PATTERN["BS_DATA"]) and (
            possible_sync != SYNC_PATTERN["MS_DATA"]
        ):
            embedded_signalling = possible_sync

        info = ((data >> 68) & ((2 ** 98 - 1) << 98)) + (data & (2 ** 98 - 1))

        return DataBurst(
            info=info, slot_type=slot_type, embedded_signalling=embedded_signalling
        )
