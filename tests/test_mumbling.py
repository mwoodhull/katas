from src.mumbling import accum


def test_returns_single_letter_for_single_letter():

    insert = "A"

    output = accum(insert)

    assert output == "A"


def test_returns_capitalised_single_letter():

    insert = "a"

    output = accum(insert)

    assert output == "A"


def test_returns_correct_response_for_two_letter_string():

    insert = "ab"

    output = accum(insert)

    assert output == "A-Bb"


def test_returns_correct_response_for_larger_strings():

    insert = "abc"

    output = accum(insert)

    assert output == "A-Bb-Ccc"


def test_returns_correct_response_when_given_mix_of_upper_and_lowercase():

    insert = "mAtT"

    output = accum(insert)

    assert output == "M-Aa-Ttt-Tttt"
