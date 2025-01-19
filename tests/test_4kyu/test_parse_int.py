from src.fourkyu.parse_int import parse_int

def test_single_digit_number():

    insert = 'zero'

    output = parse_int(insert)

    assert output == 0

    insert = 'seven'

    output = parse_int(insert)

    assert output == 7

