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
    maximum_misspell_tries = 100

    def __init__(self, sentence='', minimum_score = minimum_fuzzy_score):
        self.sentence = sentence
        self.minimum_fuzzy_score = minimum_score
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
        ranges[ChangeType.NONE] = 0.0
        return ranges

    def random_change_type(self):
        change_type = ChangeType.NONE
        new_random = np.random.uniform(0, 1, 1)
        if new_random > self.change_threshold:
            new_random = np.random.uniform(0, 1, 1)
            for key, value in self.ranges.items():
                if new_random > value:
                    change_type = key
                    break
        return change_type

    def misspell(self):
        "Generate a misspelled sentence base on the parameters"
        # Ranges of transformation where
        misspelling = []
        result = ''

        # Only accept misspellings that have a fuzzy match above the minimum score
        for t in range(0,self.maximum_misspell_tries):
            i = 0
            while i < len(self.sentence):
                change_type = self.random_change_type()
                if change_type == ChangeType.NONE:
                    misspelling.append(self.sentence[i])

                elif change_type == ChangeType.FLIP:
                    if i < (len(self.sentence) - 1):
                        misspelling.append(self.sentence[i + 1])
                        misspelling.append(self.sentence[i])
                        i += 1

                # Swap the current phoeneme for a different phoneme
                elif change_type == ChangeType.PHONEME:
                    new_phoneme, match_length = Phonemes().random_swap(self.sentence[i:-1])
                    if match_length > 0:
                        misspelling.append(new_phoneme)
                        i += match_length - 1
                    else:
                        misspelling.append(self.sentence[i])

                elif change_type == ChangeType.ADD:
                    random_letter = np.random.choice(self.letters, 1)[0]
                    misspelling.append(random_letter)
                    misspelling.append(self.sentence[i])

                elif change_type == ChangeType.SWAP:
                    random_letter = np.random.choice(self.letters, 1)[0]
                    misspelling.append(random_letter)
                # DROP case

                else:
                    pass
                i += 1

            result = ''
            for c in misspelling:
                result += c
            score = fuzz.ratio(result, self.sentence) / 100
            if (score > self.minimum_fuzzy_score) and (score < 1.0):
                break
            misspelling = []

        return result

    def is_misspelling(self, input_value):
        """Test that the input_value is a possible misspelling of the answer"""
        test = input_value.lower()
        target = self.sentence.lower()
        score = fuzz.ratio(test, target) / 100
        if score <= self.minimum_fuzzy_score:
            i = 0
            misspelling = ''
            while i < len(test):
                new_phoneme, match_length = Phonemes().random_swap(test[i:])
                if match_length > 0:
                    test_spelling = misspelling[0:i]
                    test_spelling += new_phoneme
                    test_spelling += test[i+match_length:]
                    score = fuzz.ratio(test_spelling, target) / 100
                    if score > self.minimum_fuzzy_score:
                        break
                misspelling += test[i]
                i += 1

        return score >= self.minimum_fuzzy_score
