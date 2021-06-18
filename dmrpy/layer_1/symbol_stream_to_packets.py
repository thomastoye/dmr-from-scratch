from dmrpy.constants import SYNC_PATTERN
from enum import Enum
from typing import Iterator, Optional


class State(Enum):
    OUT_OF_SYNC = 1
    RECEIVING_CACH_BURST = 2
    RECEIVING_TRAFFIC_BURST = 3


def symbol_to_decimal(symbol):
    # ETSI TS 102 361-1 10.2.2.1
    return {
        3: 1,
        1: 0,
        -1: 2,
        -3: 3,
    }[symbol]


def symbol_stream_to_packets(symbol_stream: Iterator[int]):
    SYNC_MASK: int = 0xFFFFFFFFFFFF
    CACH_BURST_MASK: int = (2 ** 24) - 1
    TRAFFIC_BURST_MASK: int = (2 ** 264) - 1

    # The index in the symbol stream, incremented with 1 for every received symbol
    index: int = 0

    # A buffer that will hold 288 bits, enough for 1 CACH burst and one traffic burst
    buffer: int = 0
    BUFFER_MASK: int = (2 ** 288) - 1

    # We start out with no sync
    state: State = State.OUT_OF_SYNC

    symbols_left_to_receive_for_burst: Optional[int] = None

    last_sync_pattern_index: Optional[int] = None

    for symbol in symbol_stream:
        buffer = ((buffer << 2) + symbol_to_decimal(symbol)) & BUFFER_MASK

        if symbols_left_to_receive_for_burst is not None:
            symbols_left_to_receive_for_burst = symbols_left_to_receive_for_burst - 1

        if (
            last_sync_pattern_index is not None
            and (index - last_sync_pattern_index) > 4800
        ):
            # No sync during the last second? Let's reset that.
            state = State.OUT_OF_SYNC
            last_sync_pattern_index = None
            symbols_left_to_receive_for_burst = None

        if state is State.OUT_OF_SYNC:
            # We don't have a sync
            # Maybe we have one now that we added another symbol to the buffer?

            if (buffer & SYNC_MASK) in SYNC_PATTERN.values():
                last_sync_pattern_index = index

                # We can already yield the CACH burst preceding this burst
                cach_burst = (buffer >> (48 + 108)) & CACH_BURST_MASK

                # A sync is part of a traffic burst
                state = State.RECEIVING_TRAFFIC_BURST
                # Since we're on the SYNC, we have 108 bits left to receive for this packet
                symbols_left_to_receive_for_burst = 108 // 2

                yield ("cach", cach_burst)

        elif state is State.RECEIVING_TRAFFIC_BURST:

            if symbols_left_to_receive_for_burst == 0:
                state = State.RECEIVING_CACH_BURST
                symbols_left_to_receive_for_burst = 12
                yield ("traffic", buffer & TRAFFIC_BURST_MASK)

        elif state is State.RECEIVING_CACH_BURST:

            if symbols_left_to_receive_for_burst == 0:
                state = State.RECEIVING_TRAFFIC_BURST
                symbols_left_to_receive_for_burst = 132
                yield ("cach", buffer & CACH_BURST_MASK)

        index = index + 1
