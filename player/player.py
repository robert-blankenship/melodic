import os
import sys
import subprocess
import wavebender
import tempfile
import math

import scale.models as ScaleModels
from scale.models import Pitch

def pitch_to_frequency(pitch):

    a4_pitch = Pitch(0, 4)
    a4_frequency = 440.0

    steps_from_a4 = ScaleModels.get_pitch_difference(a4_pitch, pitch)
    print steps_from_a4
    
    frequency = a4_frequency * math.pow(2**(1.0/12.0), steps_from_a4)
    print frequency
    return frequency

def do_cross_platform_checks():
    if os.name != "posix":
        raise Exception("Sorry bro. Your platform '%s' is not supported" % sys.platform)

    try:
        subprocess.call(["which", "play"])
    except:
        raise Exception("Sorry bro. You need to install 'play'. Just do 'brew install sox' or 'sudo apt-get install play' or some shiz like that.")

do_cross_platform_checks()

# TODO: Fix the gap in the sounds.
def play_pitch(pitch, ms):
    frequency = pitch_to_frequency(pitch)

    num_channels = 1
    bit_rate = 16
    sample_rate = 44100
    volume = 1
    data_encoding = "signed"

    sox_output_type = "raw"

    channels = ((wavebender.sine_wave(frequency),),)
    samples = wavebender.compute_samples(channels, (sample_rate/1000) * ms )
    wavebender.write_pcm(open(tempfile.gettempdir() + "/pitch", 'w+'), samples, framerate=sample_rate)

    subprocess.call(["play", "-e", data_encoding, "-r", str(sample_rate), "-v", str(volume), "-t", sox_output_type, "-c", str(num_channels), "-b", str(bit_rate), "-"], stdin=open(tempfile.gettempdir() + "/pitch"))




def run_test():
    play_pitch(Pitch(0, 4), 1000)
    play_pitch(Pitch(11, 3), 1000)
    play_pitch(Pitch(0, 4), 1000)




