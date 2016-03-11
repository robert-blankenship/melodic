#!/usr/bin/env python

#TODO: 
# - Parse command line argument for scale, get corresponding internal representation thereof.
# - Randomly select a rhythm.
# - Build melody using random notes with selected rhythmic pattern
# - Print out melody w/ rhythmic pattern.
import scale.models as ScaleModels
import rhythm.models as RhythmModels
import player.player
from functools import partial
from phrase.generator import GeneratePhrase
import argparse

def getArguments():
    parser = argparse.ArgumentParser(description="Write a melody!")
    parser.add_argument('--key', required=True, help="Set the key for the melody.")
    parser.add_argument('--scale-pattern', required=True, help="Set the scale pattern (major, minor, etc.)")
    return parser.parse_args()

def __main__():
    args = getArguments()

    def get_tonic_for_key_string(key):
        key_letter = key[0].upper()

        if ord(key_letter) < ord("A") or ord(key_letter) > ord("G"):
            raise Exception("Key '%s' is invalid. Only the keys of Ab through G# are allowed" % key)

        if len(key) > 1:
            if key[1] == "#":
                key_accidental = 1
            elif key[1] == "b":
                key_accidental = -1
            else:
                raise Exception("Key '%s' is invalid. Only the keys of Ab through G# are allowed" % key)
        else:
            key_accidental = 0

        return ScaleModels.NATURAL_TONES_BY_LETTER[key_letter] + key_accidental

    def get_scale_pattern_for_string(scale_pattern_string):
        return {
                'major': ScaleModels.ScalePatterns.Major,
                'natural-minor': ScaleModels.ScalePatterns.NaturalMinor,
                'harmonic-minor': ScaleModels.ScalePatterns.HarmonicMinor,
                'major-pentatonic': ScaleModels.ScalePatterns.MajorPentatonic,
                'minor-pentatonic': ScaleModels.ScalePatterns.MinorPentatonic
        }[scale_pattern_string.lower()]

    tonic = get_tonic_for_key_string(args.key)
    scale_pattern = get_scale_pattern_for_string(args.scale_pattern)

    scale = ScaleModels.Scale(ScaleModels.Pitch(tonic,4), scale_pattern)

    map(partial(player.player.play_pitch, ms=1000), scale.notes)

    GeneratePhrase(scale)    

#RhythmModels.test1()
__main__()

