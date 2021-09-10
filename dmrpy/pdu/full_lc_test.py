from dmrpy.util.numpy_bit_array_to_int import numpy_bit_array_to_int
from dmrpy.pdu.voice_burst import VoiceBurst
from dmrpy.pdu.full_lc import FullLC
import numpy as np
from dmrpy.util.to_numpy_bit_array import to_numpy_bit_array
from numpy.testing import assert_array_equal

# TODO This file is just experimentation, clean up

VOICE_SUPERFRAME = [
    # Data head (7.1.1): 0x2B6004101F842DD00DF07D41046DFF57D75DF5DE30152E2070B20F803F88C695E2
    # See 7.1.3: A: Sync, B-E: Link Control, F: Reverse Channel Opportunity
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6BB9E881526755FD7DF75F7173002A6BB9E881526173002A6A
    ),  # A
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6BB9E881526134E0F060691173002A6BB9E881526173002A6A
    ),  # B
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6BB9E881526171711004774173002A6BB9E881526173002A6A
    ),  # C
    VoiceBurst.create_from_burst_binary(
        0xB9E881526173002A6B954BE6500170C03181B74310B00777A6C6CB53732789483A
    ),  # D
    VoiceBurst.create_from_burst_binary(
        0x865AE7617555B50601B758E665115175A0F4E07124815001FFF5A337706128A7CA
    ),  # E
    VoiceBurst.create_from_burst_binary(
        0xEEE7817574614DF2FFCCF4A05511100000000E243059E7F9E908A0756202CCD622
    ),  # F
    # Voice term (7.1.2): 0x2B0F04C41F342DA80D807DE104ADFF57D75DF5D965012D1877D203C03788DF95D1
]

# Voice superframe example:
# A: (Sync)
# B:  lcss=0x1 - 0x4e0f0606
# C:  lcss=0x3 - 0x17110047
# D:  lcss=0x3 - 0x0c03181b
# E:  lcss=0x2 - 0x175a0f4e
# F: (lcss=0x0 - 0x00000000)

EXPECTED_LC = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    0,
    1,
]

# See 7.1.3.1

# Successive embedded signalling fields of voice bursts (B-E) in a superframe

EMBEDDED_SIGNALLING = [0x4E0F0606, 0x17110047, 0x0C03181B, 0x175A0F4E]

## 1. De-interleave

# See B.2.1
# We have 4 embedded bursts => N=8 => 7*LC info + 1*simple parity check
# The BPTC encoding matrix has 8 rows, 16 columns = 128 bits
# The transmit matrix has      4 rows, 32 columns = 128 bits


transmit_matrix = np.array([to_numpy_bit_array(x, 32) for x in EMBEDDED_SIGNALLING])

# Calculated manually from transmit matrix
bptc_encode_matrix = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    ]
)


def test_transmit_matrix_to_bptc_encode_matrix():
    assert_array_equal(transmit_matrix.reshape(16, 8).transpose(), bptc_encode_matrix)


def test_bptc_encode_matrix_to_transmit_matrix():
    assert_array_equal(bptc_encode_matrix.transpose().reshape(4, 32), transmit_matrix)


def extract_lc(a):
    return np.concatenate(
        (
            a[0][0:11],
            a[1][0:11],
            a[2][0:10],
            a[3][0:10],
            a[4][0:10],
            a[5][0:10],
            a[6][0:10],
        )
    )


def extract_checksum_bits(a):
    # See B.2.1
    return np.array(
        [
            a[2][10],
            a[3][10],
            a[4][10],
            a[5][10],
            a[6][10],
        ]
    )


def test_extract_lc():
    assert_array_equal(
        extract_lc(bptc_encode_matrix),
        EXPECTED_LC,
    )


def test_extract_checksum_bits():
    assert_array_equal(extract_checksum_bits(bptc_encode_matrix), [0, 1, 1, 0, 0])


def test_full_lc_create_from_binary():
    lc = FullLC.create_from_embedded_signalling_binary(0x1020000C302F9BE5, 0xC)

    assert lc.pf == 0
    assert lc.reserved == 0
    assert lc.flco == 0
    assert (
        lc.fid == 0x10
    )  # Strange as fid should be 0x0 for flco=0x0 but this seems to be a valid packet
    assert lc.cs_5bit == 0xC
    assert lc.data == 0x20000C302F9BE5
    assert lc.raw() == 0x1020000C302F9BE5
    assert lc.checksum_matches()


def test_create_from_superframe():
    lc = FullLC.create_from_superframe(VOICE_SUPERFRAME)

    # assert VOICE_SUPERFRAME[1].embedded_signalling == 0x4e0f0606
    # assert VOICE_SUPERFRAME[2].embedded_signalling == 0x17110047
    # assert VOICE_SUPERFRAME[3].embedded_signalling == 0x0c03181b
    # assert VOICE_SUPERFRAME[4].embedded_signalling == 0x175a0f4e

    # A: (Sync)
    # B:  lcss=0x1 - 0x4e0f0606
    # C:  lcss=0x3 - 0x17110047
    # D:  lcss=0x3 - 0x0c03181b
    # E:  lcss=0x2 - 0x175a0f4e
    # F: (lcss=0x0 - 0x00000000)

    # assert numpy_bit_array_to_int(EXPECTED_LC) == 0

    assert lc.pf == 0
    assert lc.reserved == 0
    assert lc.flco == 0
    assert lc.fid == 0x20
    assert lc.cs_5bit == 0x18
    assert lc.data == 0x400018605F37CA
    assert lc.raw() == 0x20400018605F37CA
    # assert lc.checksum_matches() TODO


# Now we need to reshape the "transmit matrix" (actually the received matrix in our case)

## 2. BPTC

# Hamming(16,11,4)

## 3. Split to Link Control (72 bits) and checksum (5 bits), validate checksum

# 5-bit Checksum (CS) is defined in clause B.3.11.
