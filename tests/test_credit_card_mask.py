from src.credit_card_mask import credit_card_mask


def test_full_password_returned_if_less_than_5_characters():

    entry = "cat"
    output = credit_card_mask(entry)

    assert output == "cat"

    entry = ""
    output = credit_card_mask(entry)

    assert output == ""


def test_returns_hidden_password_if_over_5_characters():

    entry = "0123456789"
    output = credit_card_mask(entry)

    assert output == "######6789"

    entry = "matthewisthegreatestcoderintheworld"
    output = credit_card_mask(entry)

    assert output == "###############################orld"
