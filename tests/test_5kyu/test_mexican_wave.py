from src.fivekyu.mexican_wave import mexican_wave

def test_returns_empty_list_when_empty_string_passed_in():

    insert = ''

    output = mexican_wave(insert)

    assert output == ['']

def test_returns_captialised_letter_when_single_letter_string_passed_in():

    insert = 'a'

    output = mexican_wave(insert)

    assert output == ['A']

def test_returns_correct_response_for_whole_word():

    insert = 'matt'

    output = mexican_wave(insert)

    assert output == ['Matt', 'mAtt', 'maTt', 'matT']