from src.return_negative import return_negative


def test_0_returns_0():
    entry = 0
    result = return_negative(entry)

    assert result == 0


def test_postive_number_returns_negative_number():

    entry = 1
    result = return_negative(entry)

    assert result == -1

    entry = 43588
    result = return_negative(entry)

    assert result == -43588


def test_negative_number_returns_negative_numer():

    entry = -1
    result = return_negative(entry)

    assert result == -1

    entry = -43588
    result = return_negative(entry)

    assert result == -43588
