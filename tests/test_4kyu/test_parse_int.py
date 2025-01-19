from src.fourkyu.parse_int import parse_int

def test_single_digit_number():

    insert = 'zero'

    output = parse_int(insert)

    assert output == 0

    insert = 'seven'

    output = parse_int(insert)

    assert output == 7

    insert = 'nine'

    output = parse_int(insert)

    assert output == 9

def test_teens():

    insert = 'eleven'

    output = parse_int(insert)

    assert output == 11

    insert = 'fifteen'

    output = parse_int(insert)

    assert output == 15

    insert = 'eighteen'

    output = parse_int(insert)

    assert output == 18

def test_tens():

    insert = 'ten'

    output = parse_int(insert)

    assert output == 10

    insert = 'sixty'

    output = parse_int(insert)

    assert output == 60

def test_powers():

    insert = 'hundred'

    output = parse_int(insert)

    assert output == 100

    insert = 'thousand'

    output = parse_int(insert)

    assert output == 1000

    insert = 'million'

    output = parse_int(insert)

    assert output == 1000000000