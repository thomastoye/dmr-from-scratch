from dmrpy.layer_1.rrcos_filter import RRCOS_FILTER
from dmrpy.layer_1.symbol_stream_to_packets import symbol_stream_to_packets
from typing import Iterator
import numpy as np
from scipy.signal import convolve, resample

TARGET_FS = 48000
SAMPLES_PER_SYMBOL = 10


def find_best_phase_offset(wave, samples_per_symbol: int):
    # We use the standard deviation as a heuristic for the "how nicely are they split into bins?"
    # Seems to work well enough

    best_offset = np.argmax(
        [
            np.std(wave[offset::samples_per_symbol])
            for offset in range(0, samples_per_symbol)
        ]
    )

    return best_offset


def digitize(arr, bins):
    """Digitize an array of samples: turn them into symbols. But also add the certainity (how close it is to the middle of the bin). This helps to evaluate signal quality"""
    middles = [x + ((y - x) / 2) for (x, y) in zip(bins, bins[1:])]
    half_bin_width = (bins[1] - bins[0]) / 2

    # Bin the samples and convert them to a bitstream

    # np.digitize will assign the number of the bin
    # This map maps bin numbers to dibits
    # See ETSI TS 102 361-1 Table 10.3
    DIGITIZED_TO_SYMBOL = {1: +3, 2: +1, 3: -1, 4: -3}

    symbols = np.array(
        [
            {
                "symbol": DIGITIZED_TO_SYMBOL[bin],
                "certainity": 1 - (abs(middles[bin - 1] - element) / half_bin_width),
            }
            for (bin, element) in zip(np.digitize(arr, bins, right=True), arr)
        ]
    )

    return symbols


def filtered_list_to_symbols(filtered: Iterator[int], samples_per_symbol: int):
    offset = find_best_phase_offset(filtered, samples_per_symbol)
    sampled = filtered[offset::samples_per_symbol]

    # Generate bins to sort samples
    middle = (np.quantile(sampled, 0.05) + np.quantile(sampled, 0.95)) / 2
    bins = [
        np.min(sampled) - 1,
        (np.min(sampled) + middle) / 2,
        middle,
        (np.max(sampled) + middle) / 2,
        np.max(sampled) + 1,
    ]

    return digitize(sampled, bins)


def audio_stream_to_symbols(audio_stream: Iterator[int], fs: int):
    # TODO make this work with iterators/in a streaming way
    resampled = resample(audio_stream, int((TARGET_FS / fs) * len(audio_stream)))
    filtered = convolve(resampled, RRCOS_FILTER, mode="same")

    return np.array(
        [
            symbol
            for l in np.array_split(filtered, len(filtered) // TARGET_FS)
            for symbol in filtered_list_to_symbols(l, SAMPLES_PER_SYMBOL)
        ]
    )
