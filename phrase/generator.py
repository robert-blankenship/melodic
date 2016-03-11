
import rhythm.models as RhythmModels
import random

def getRandomRhythm():
    all_pattern_keys = RhythmModels.TwoBarRhythms.get_all_patterns()
    pattern_key = random.choice(all_pattern_keys)
   
    return getattr(RhythmModels.TwoBarRhythms, pattern_key)

class GeneratePhrase:
    def __init__(self, scale):
        print scale
        randomRhythm = getRandomRhythm()

        phrase = list()

        for element in randomRhythm:
            if element == 0:
                phrase.append("")
            elif element == 1:
                phrase.append(random.choice(scale.notes))


        print phrase
