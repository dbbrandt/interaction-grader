from interactiongrader import Phonemes

pn = Phonemes()

def test_alternate_list():
    alts = pn.alternate_list('aigh')
    assert len(alts) == 10

def test_is_alternate():
    assert pn.is_alternate('aigh', 'eigh')

def test_random_swap():
    pn_df = pn.df
    assert len(pn_df) == 221
    new_value, match_length = pn.random_swap('l')
    assert new_value == 'll'
    assert match_length == 1

    new_value, match_length = pn.random_swap('q')
    assert new_value == ''
    assert match_length == 0

def test_swap_list():
    alts = pn.swap_list('l')
    assert len(alts) == 1
    assert alts[0][0] == 'll'
    assert alts[0][1] == 1

    alts = pn.swap_list('k')
    assert len(alts) == 7
    alt_list = [a[0] for a in alts]
    assert 'c' in alt_list

    alts = pn.swap_list('aigh')
    assert len(alts) == 30
    alt_list = [a[0] for a in alts]
    assert 'ae' in alt_list
