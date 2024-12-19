from src.high_and_low import high_and_low

def test_returns_highest_and_lowest_when_2_long():

    insert = "1 2"

    output = high_and_low(insert)

    assert output == "2 1"

def test_returns_highest_and_lowest_when_longer_than_2():

    insert = "1 4 -16 4 22 99"

    output = high_and_low(insert)

    assert output == "99 -16"

def test_returns_same_number_when_only_one_long():

    insert = "1 1"

    output = high_and_low(insert)

    assert output == "1 1"

def test_returns_correct_output_when_multiple_max_or_min():

    insert = "1 1 6 9 12 12"

    output = high_and_low(insert)

    assert output == "12 1"