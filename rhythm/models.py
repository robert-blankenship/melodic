# TODO:

# - representation of a beat (temporal musical element)
# - representation of a rhythmic pattern
# - listing of rhytmic patterns


#class RhythmicPattern():
#    return [];

#class Beat():
#    return 

#class Silence():
class Do:
    def __init__(self):
        pass

class Persist:
    def __init__(self):
        pass

class Release:
    def __init__(self):
        pass

class Rhythm:
    def __init__(self, beats, beats_per_bar, rhythmic_pattern):
        if beats % beats_per_bar != 0:
            raise Exception("Rhythms that end in the middle of a bar are not supported (currently).")

        self.beats = beats
        self.beats_per_bar = beats_per_bar
        self.pattern = rhythmic_pattern

class RhythmicPatterns:
    @staticmethod
    def double_time(divisions):
        return [(1, 1)] * divisions

    @staticmethod
    def half(divisions):
        return [(1),(0)]  * (divisions / 2)

    @staticmethod
    def syncopated(divisions):
        return [(0, 1)] * divisions
    
    @staticmethod
    def every(divisions):
        return [(1)] * divisions 

    @staticmethod
    def every_other(divisions):
        if divisions % 3 == 0:
            return [(0),(1),(0)] * (divisions / 3)
        elif divisions % 2 == 0:
            return [(0),(1)] * (divisions / 2)

    @staticmethod
    def two_one(divisions):
        return [(2, 1)] * divisions

    @staticmethod
    def one_two(divisions):
        return [(1, 2)] * divisions

    @staticmethod
    def once(divisions):
        return [(1)] + [(0)] * (divisions - 1)

    @staticmethod
    def none(divisions):
        return [0] * divisions

class TwoBarRhythms:
    half = RhythmicPatterns.half
    every = RhythmicPatterns.every
    every_other = RhythmicPatterns.every_other
    once = RhythmicPatterns.once
    none = RhythmicPatterns.none

    a_a_aaaa = half(4) + every(4)
    a_a_aa__ = half(4) + every(2) + none(2)
    a___aaaa = once(4) + every(4)
    a___aa__ = once(4) + every(2) + none(2)
    a___a___ = once(4) + once(4)
    _a_aa___ = every_other(4) + once(4)

    @staticmethod
    def get_all_patterns():
        properties = dir(TwoBarRhythms)
        pattern_keys = filter(lambda x: x not in [
            "__doc__",
            "__module__",
            "half",
            "every",
            "every_other",
            "once",
            "none",
            "get_all_patterns"
        ], properties)

        return pattern_keys


def test1():
    print TwoBarRhythms.a_a_aaaa
    print TwoBarRhythms.a___aaaa
    print TwoBarRhythms._a_aa___

