from scipy.io import wavfile
from dmrpy.project_root import get_module_root

FIXTURE_SAMPLE_RATE, FIXTURE = wavfile.read(
    get_module_root() / "fixtures" / "SDRSharp_20160101_231914Z_12kHz_real.wav"
)
