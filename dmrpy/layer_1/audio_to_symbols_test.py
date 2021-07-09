from dmrpy.fixtures.fixtures import FIXTURE, FIXTURE_SAMPLE_RATE
from dmrpy.layer_1.audio_to_symbols import audio_stream_to_symbols
from numpy.testing import assert_array_equal


def test_audio_stream_to_symbols():
    result = audio_stream_to_symbols(
        FIXTURE[0 : FIXTURE_SAMPLE_RATE * 3], FIXTURE_SAMPLE_RATE
    )
    assert result.shape == (4800 * 3,)
    assert_array_equal(
        result[0:20],
        [
            {"symbol": 1, "certainity": 0.6743079383692678},
            {"symbol": 1, "certainity": 0.6015634397563788},
            {"symbol": 3, "certainity": 0.7684642115814788},
            {"symbol": -1, "certainity": 0.8090187601599226},
            {"symbol": 1, "certainity": 0.9696553883895588},
            {"symbol": 3, "certainity": 0.5327646441430528},
            {"symbol": 1, "certainity": 0.9542989850432748},
            {"symbol": -3, "certainity": 0.8821460948604771},
            {"symbol": 1, "certainity": 0.8821619091702755},
            {"symbol": 1, "certainity": 0.9202129017913234},
            {"symbol": -3, "certainity": 0.6598463677410102},
            {"symbol": -3, "certainity": 0.45677552038953284},
            {"symbol": -1, "certainity": 0.8398247633040649},
            {"symbol": 3, "certainity": 0.7004065714009378},
            {"symbol": 1, "certainity": 0.42295936340373974},
            {"symbol": 3, "certainity": 0.742130499281096},
            {"symbol": -1, "certainity": 0.7753563175893784},
            {"symbol": -1, "certainity": 0.5366334303092459},
            {"symbol": -1, "certainity": 0.9321823528299901},
            {"symbol": 3, "certainity": 0.957299107392927},
        ],
    )
