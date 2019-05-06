from interactiongrader import Answer
from interactiongrader import ChangeType
from fuzzywuzzy import fuzz

def test_calculate_ranges():
    ans = Answer()
    ranges = ans.calculate_ranges()

    assert ans.sentence == ''
    assert ranges[ChangeType.FLIP] == 0.75

def test_random_change_type():
    ans = Answer()
    change = ans.random_change_type()

    assert change in ChangeType

def test_misspell():
    ans = Answer('Sample test')
    misspelled = ans.misspell()
    score = fuzz.ratio(misspelled, ans.sentence)

    assert ans.sentence == 'Sample test'
    assert ans.sentence != misspelled
    assert score >= ans.minimum_fuzzy_score

def test_is_misspelling():
    ans = Answer('Cate Blanchett')
    assert ans.is_misspelling('Kate Blancette')

    ans = Answer('Minnie Driver')
    assert ans.is_misspelling('Minny Driver')

    ans = Answer('Joaquin Phoenix')
    assert ans.is_misspelling('Joakin Pheonix')

