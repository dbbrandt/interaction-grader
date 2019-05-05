from enum import Enum
from fuzzywuzzy import fuzz
from .Phonemes import Phonemes
import numpy as np
from .Changetype import ChangeType

class Answer():
    """The answer to an interaction."""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]


    # Misspelling transformation percentage defaults - must add up to 1
    flip_percent = 0.25
    phoneme_percent = 0.15
    add_percent = 0.10
    swap_percent = 0.25
    drop_percent = 0.25

    change_threshold = 0.85
    minimum_fuzzy_score = 0.90
    maximum_misspell_tries = 10

    def __init__(self, text):
        self.text = text
        self.ranges = self.calculate_ranges()

    def calculate_ranges(self):
        self.ranges = {}
        flip = 1 - self.flip_percent
        phoneme = flip - self.phoneme_percent
        add = phoneme - self.add_percent
        swap = add - self.swap_percent
        drop = swap - self.drop_percent

        ranges = {}
        ranges[ChangeType.FLIP] = flip
        ranges[ChangeType.PHONEME] = phoneme
        ranges[ChangeType.ADD] = add
        ranges[ChangeType.SWAP] = swap
        ranges[ChangeType.DROP] = drop
        ranges[ChangeType.NONE] = 0
        return ranges

    def random_change_type(self):
        change_type = ChangeType.NONE
        new_random = np.random.uniform(0, 1, 1)
        if new_random > self.change_threshold:
            new_random = np.random.uniform(0, 1, 1)
            for key, value in enumerate(self.ranges):
                if new_random > value:
                    change_type = key
                    break
        return change_type

    def misspell(self, sentence):
        "Generate a misspelled sentence base on the parameters"
        # Ranges of transformation where
        misspelling = []
        result = ''
        phoneme = Phonemes()

        # Only accept misspellings that have a fuzzy match above the minimum score
        for t in range(0,self.maximum_misspell_tries):
            i = 0
            while i < len(sentence):
                change_type = self.random_change_type()
                # No change
                if change_type == ChangeType.NONE:
                    # print("No change")
                    misspelling.append(sentence[i])
                elif change_type == ChangeType.FLIP:
                    if i < (len(sentence) - 1):
                        # print("Flip letters {}".format(sentence[i]))
                        misspelling.append(sentence[i + 1])
                        misspelling.append(sentence[i])
                        i += 1
                elif change_type == ChangeType.PHONEME:
                    # print("Swap phoneme {}".format(sentence[i]))
                    misspelling.append(phoneme.random_swap(sentence[i]))
                elif change_type == ChangeType.ADD:
                    # print("Random add letter {}".format(sentence[i]))
                    random_letter = np.random.choice(self.letters, 1)[0]
                    misspelling.append(random_letter)
                    misspelling.append(sentence[i])
                elif change_type == ChangeType.SWAP:
                    # print("Random swap letter {}".format(sentence[i]))
                    random_letter = np.random.choice(self.letters, 1)[0]
                    misspelling.append(random_letter)
                # DROP case
                else:
                    pass
                i += 1
            result = ''
            for c in misspelling:
                result += c
            score = fuzz.ratio(result, sentence) / 100
            if score > self.minimum_fuzzy_score:
                break
            misspelling = []

        return result

