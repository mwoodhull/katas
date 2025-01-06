from src.initials import initials


def test_two_word_titled_name_returns_correctly():

    insert = "Code Wars"

    output = initials(insert)

    assert output == "C.Wars"


def test_more_than_two_word_name():

    insert = "Barack Hussein Obama"

    output = initials(insert)

    assert output == "B.H.Obama"


def test_name_provided_all_lower_case():

    insert = "barack hussein obama"

    output = initials(insert)

    assert output == "B.H.Obama"


def test_name_that_is_all_uppercase():

    insert = "BARACK HUSSEIN OBAMA"

    output = initials(insert)

    assert output == "B.H.Obama"


def test_longer_names():

    insert = "george smith peter rabbit harry gregg david scott"

    output = initials(insert)

    assert output == "G.S.P.R.H.G.D.Scott"
