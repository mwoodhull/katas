from src.fivekyu.mexican_wave import mexican_wave


def test_returns_empty_list_when_empty_string_passed_in():

    insert = ""

    output = mexican_wave(insert)

    assert output == []


def test_returns_captialised_letter_when_single_letter_string_passed_in():

    insert = "a"

    output = mexican_wave(insert)

    assert output == ["A"]


def test_returns_correct_response_for_whole_word():

    insert = "matt"

    output = mexican_wave(insert)

    assert output == ["Matt", "mAtt", "maTt", "matT"]


def test_ignores_space_characters():

    insert = "i am matt"

    output = mexican_wave(insert)

    assert output == [
        "I am matt",
        "i Am matt",
        "i aM matt",
        "i am Matt",
        "i am mAtt",
        "i am maTt",
        "i am matT",
    ]


def test_ignores_other_irrelevant_characters():

    insert = "m!att"

    output = mexican_wave(insert)

    assert output == ["M!att", "m!Att", "m!aTt", "m!atT"]
