from src.fourkyu.parse_int import parse_int


def test_single_digit_number():

    insert = "zero"

    output = parse_int(insert)

    assert output == 0

    insert = "seven"

    output = parse_int(insert)

    assert output == 7

    insert = "nine"

    output = parse_int(insert)

    assert output == 9


def test_teens():

    insert = "eleven"

    output = parse_int(insert)

    assert output == 11

    insert = "fifteen"

    output = parse_int(insert)

    assert output == 15

    insert = "eighteen"

    output = parse_int(insert)

    assert output == 18


def test_tens():

    insert = "ten"

    output = parse_int(insert)

    assert output == 10

    insert = "sixty"

    output = parse_int(insert)

    assert output == 60


def test_powers():

    insert = "hundred"

    output = parse_int(insert)

    assert output == 100

    insert = "thousand"

    output = parse_int(insert)

    assert output == 1000

    insert = "million"

    output = parse_int(insert)

    assert output == 1000000000


def test_tens_units_combination():

    insert = 'twenty three'

    output = parse_int(insert)

    assert output == 23

    insert = 'ninety six'

    output = parse_int(insert)

    assert output == 96

    insert = 'seventy one'

    output = parse_int(insert)

    assert output == 71

def test_single_hundreds_tens_units_combination():

    insert = 'hundred thirty four'

    output = parse_int(insert)

    assert output == 134

def test_multiple_hundreds_tens_units_combination():

    insert = 'nine hundred fifty eight'

    output = parse_int(insert)

    assert output == 958

    insert = 'six hundred thirty two'

    output = parse_int(insert)

    assert output == 632 

def test_can_handle_ands():

    insert = 'seven hundred and twenty two'

    output = parse_int(insert)

    assert output == 722

def test_can_handle_hyphens():

    insert = 'two hundred forty-five'

    output = parse_int(insert)

    assert output == 245

    insert = 'six-hundred and ninety-one'

    output = parse_int(insert)

    assert output == 691

def test_thousands_hundreds_tens_units_combination():

    insert = 'thousand seven hundred fifty six'

    output = parse_int(insert)

    assert output == 1756

def test_multiple_thousands_hundreds_tens_units_combination():

    insert = 'seven thousand two hundred and forty-nine'

    output = parse_int(insert)

    assert output == 7249

def test_multiple_thousand_and_one():

    insert = 'six thousand and one'

    output = parse_int(insert)

    assert output == 6001