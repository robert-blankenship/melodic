import sys
import subprocess
import wavebender
import tempfile

def pitch_to_frequency(pitch):
    def steps_from_a4(pitch):
        return -2

    a4_frequency = 440.0
    twelth_root_of_twelve = math.pow(12, 1.0/12)

    return a4_frequency * math.pow(twelth_root_of_twelve, steps_from_a4(pitch))

def do_cross_platform_checks():
    print "sys.platform %s" % sys.platform
    print "os.name: %s" % os.name

    platform_key = sys.platform

    if os.name != "posix":
        raise Exception("Sorry bro. Your platform %s is not supported" % platform_key)

    try:
        subprocess.check_call("which play")
    except:
        raise Exception("Sorry bro. You need to install 'play'. Just do 'brew install sox' or 'sudo apt-get install play' or some shiz like that.")

do_cross_platform_checks()

def play_pitch(pitch, duration):
    frequency = pitch_to_frequency(pitch)

    channels = 1
    bit_rate = 16
    sample_rate = 44100
    volume = 1

    sox_output_type = "raw"

    stream = tempfile.TemporaryFile()

    wavebender

    subprocess.call(["play", "-v", volume, "-t", sox_output_type, "-c", channels, "-b", bit_rate])
    




