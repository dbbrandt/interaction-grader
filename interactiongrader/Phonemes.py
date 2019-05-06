import numpy as np
import pandas as pd
import random

phoneme_list = [[1, ['b', 'bb']],
                [2,['d', 'dd', 'ed']],
                [3,['f','ff','ph','gh','lf','ft']],
                [4,['g','gg','gh','gu','gue']],
                [5,['h','wh']],
                [6,['j','ge','g','dge','di','gg']],
                [7,['k','c','ch','cc','lk','qu','ck','x']],
                [8,['l','ll']],
                [9,['m','mm','mb','mn','lm']],
                [10,['n','nn','kn','gn','pn']],
                [11,['p','pp']],
                [12,['r','rr','wr','rh']],
                [13,['s','ss','c','sc','ps','st','ce','se']],
                [14,['t','tt','th','ed']],
                [15,['v','f','ph','ve']],
                [16,['w','wh','u','o']],
                [17,['z','zz','s','ss','x','ze','se']],
                [18,['s','si','z']],
                [19,['ch','tch','tu','ti','te']],
                [20,['sh','ce','s','ci','si','ch','sci','ti']],
                [21,['ng','n','ngue']],
                [22,['y','i','j']],
                [23,['a','ai','au']],
                [24,['a','ai','eigh','aigh','ay','er','et','ei','au','ea','ey']],
                [25,['e','ea','u','ie','ai','a','eo','ei','ae']],
                [26,['e','ee','ea','y','ey','oe','ie','i','ei','eo','ay']],
                [27,['i','e','o','u','ui','y','ie']],
                [28,['i','y','igh','ie','uy','ye','ai','is','eigh']],
                [29,['a','ho','au','aw','ough']],
                [30,['o','oa','oe','ow','ough','eau','oo','ew']],
                [31,['o','oo','u','ou']],
                [32,['u','o','oo','ou']],
                [33,['o','oo','ew','ue','oe','ough','ui','oew','ou']],
                [34,['oi','oy','uoy']],
                [35,['ow','ou','ough']],
                [36,['a','er','i','ar','our','ur']],
                [37,['air','are','ear','ere','eir','ayer']],
                [38,['ir','er','ur','ear','or','our','yr']],
                [39,['aw','a','or','oor','ore','oar','our','augh','ar','ough','au']],
                [40,['ear','eer','ere','ier']],
                [41,['ure','our']]]

class Phonemes:
    """ Phonemes class for representing the english language phonenes.
    This class helps identify phonemens and replace a phoneme in a sentence or word.
    """

    def __init__(self):
        self.df = self._to_dataframe()

    def _to_dataframe(self):
        "Returns the phoneme list as a dataframe one per row"
        flat = []
        for val in phoneme_list:
            for p in val[1]:
                flat.append([val[0], p])
        df = pd.DataFrame(flat)
        df.columns = ['id', 'value']
        return df


    def alternate_list(self, phoneme):
        """Returns a list of phonemes that match the one passed in"""
        alts = []
        found = self.df[self.df['value'] == phoneme]

        if len(found) > 0:
            # Get all the ids to phoneme sets that include the input value
            found_ids = found['id'].values

            # Get all phonemes from the related sets
            related_rows = self.df[self.df['id'].isin(found_ids)]
            alt_phonemes = related_rows['value'].values
            alts = np.unique(alt_phonemes).tolist()
            # remove the input_value insuring a different phoneme value is choosen
            alts.remove(phoneme)

        return alts

    def is_alternate(self, phoneme, alt):
        """"Checks that the alt is a valid alternate phoneme"""
        return alt in self.alternate_list(phoneme)


    def random_swap(self, input_value):
        """
        Returns a random phoneme from any set that includes the input character

        :param string: any phoneme string incuding single letters
        :return: A random phoneme from a phoneme set that excludes the input string
                 The length of the sub_string being swapped
        """

        new_phoneme = ''
        length_replaced = 0
        swaps = self.swap_list(input_value)
        if len(swaps) > 0:
            index = random.randint(1,len(swaps)) - 1
            random_swap= swaps[index]
            new_phoneme = random_swap[0]
            length_replaced = random_swap[1]

        return new_phoneme, length_replaced


    def swap_list(self, input_value):
        """
        Returns a complete list phonemes based on the first four letters of a string
        Phonemes can range from 1 to four chaaracers so each character set is evaluated for swaps
        The return result includes the number of characters swapped.

        :param string: a string starting with possible phonemes to lookup
        :return: all possible phonemes and the sub-string they replace.

        """

        swap_values = []
        # Replace no more than the input
        max_len = min(4,len(input_value))
        # Matched the longest phoneme in the input
        # Start matching phoneme from 4 character match to single character match.
        results = []
        for i in range(max_len,0,-1):
            match_str = str(input_value[0:i])
            found = self.df[self.df['value'] == match_str]
            if len(found) > 0:
                alt_list = list(np.unique(self.alternate_list(match_str)))
                for alt in alt_list:
                    prefix_match = alt == input_value[:len(alt)]
                    if (alt not in results) and (not prefix_match):
                        results.append(alt)
                        swap_values.append([alt, i])

        return swap_values
