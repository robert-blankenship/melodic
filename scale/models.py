#TODO: 

# - Internal representation of a note (sound with a specific pitch)
# - Internal mapping of scale symbol and collection of notes (or generation thereof)

#  if not isinstance(frequency, int):
#            raise Exception("frequency must be an integer")

CHROMATIC_SCALE = range(12)

NATURAL_TONES = {
        0: "A",
        2: "B",
        3: "C",
        5: "D",
        7: "E",
        8: "F",
        10: "G"
}
NATURAL_TONES_BY_LETTER = {v: k for k, v in NATURAL_TONES.items()}

NO_INTONATION=""
FLAT_INTONATION="b"
SHARP_INTONATION="#"

HALF_STEP = 1
WHOLE_STEP = 2

# TODO: Consider cases where step is larger than 1 octave, e.g., +14 or -20
def modifyPitchBy(pitch, step):
    if pitch.tone + step >= 12:
        return Pitch((pitch.tone + step) % 12, pitch.octave + 1)
    elif pitch.tone + step < 0:
        return Pitch((pitch.tone + step) + 12, pitch.octave - 1)
    else:
        return Pitch(pitch.tone + step, pitch.octave)

class Pitch:
    def __repr__(self):
        return self.to_symbol()

    # TODO: Consider cases where tone > 11?
    def __init__(self, tone, octave):
        if tone not in CHROMATIC_SCALE:
            raise Exception("Tone must be an integer in %s" % CHROMATIC_SCALE)
        if not isinstance(octave, int) and octave > 0:
            raise Exception("Octave (%s) must be a positive integer" % octave)

        self.tone = tone
        self.octave = octave
     
    # TODO: Think about how this will work for different scales.
    def get_intonation(self):
        if self.tone in NATURAL_TONES:
            return NO_INTONATION
        else:
            return SHARP_INTONATION

    # NOTE: This is coupled to the above function.
    def get_note_letter(self):
        if self.tone in NATURAL_TONES:
            return NATURAL_TONES[self.tone]
        else:
            return NATURAL_TONES[self.tone - 1]

    # TODO: Think about how this will work in keys...
    def to_symbol(self, key=None):
        return "%s%s%s" % (self.get_note_letter(), self.octave, self.get_intonation())


half=HALF_STEP
whole=WHOLE_STEP
minor_third=WHOLE_STEP + HALF_STEP

# Scale patterns
class ScalePatterns:
    Major         = [whole, whole, half,  whole, whole, whole]
    NaturalMinor  = [whole, half , whole, whole, half,  whole]
    HarmonicMinor = [whole, half , whole, whole, whole,  half]
    
    MajorPentatonic    = [whole, whole, minor_third, whole]
    MinorPentatonic    = [minor_third, whole, whole, minor_third ]
    # Scales that are different going down than up??? Is that even a scale (in the strictest sense, as opposed to a melodic pattern)?

class Scale:
    def __init__(self, tonic, scale_pattern):
        if not isinstance(tonic, Pitch):
            raise Exception("Tonic must be an instance of Pitch")

        self.tonic = tonic
        self.pattern = scale_pattern

        self.notes = [ tonic ]

        for step in self.pattern:
            next_pitch = modifyPitchBy(self.notes[-1], step)
            self.notes.append(next_pitch)

    def __repr__(self):
        return str(self.notes)

def test1():
    for tone in NATURAL_TONES:
        print Pitch(tone, 0)

    print ScalePatterns.Major
    print ScalePatterns.NaturalMinor
    print ScalePatterns.HarmonicMinor

    print Scale(Pitch(0, 0), ScalePatterns.Major)
    print Scale(Pitch(2, 0), ScalePatterns.Major)
    print Scale(Pitch(10, 0), ScalePatterns.NaturalMinor)
    print Scale(Pitch(10, 0), ScalePatterns.MajorPentatonic)
    print Scale(Pitch(10, 0), ScalePatterns.MinorPentatonic)
