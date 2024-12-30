from src.ascii_total import uni_total

def test_returns_ascii_total_when_single_character():

    insert = 'a'

    output = uni_total(insert)

    assert output == 97

def test_returns_total_ascii_for_multiple_letters():

    insert = 'aaa'

    output = uni_total(insert)

    assert output == 291

    insert = 'abc'

    output = uni_total(insert)

    assert output == 294

def test_can_handle_uppercase_and_different_symbols():

    insert = '234oij^35G267££'
    
    output = uni_total(insert)

    assert output == 1229