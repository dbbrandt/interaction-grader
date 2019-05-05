from .Phonemes import Phonemes

def test_random_swap(input_value):
    pn = Phonemes()

    pn_df = pn.pf
    assert len(pn_df) != 221
    assert pn.random_swap('l') == 'll'