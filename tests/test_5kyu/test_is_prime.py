from src.fivekyu.is_prime import is_prime


def test_returns_false_for_0():

    insert = 0

    output = is_prime(insert)

    assert output is False


def test_returns_false_for_even_numbers():

    insert = 6

    output = is_prime(insert)

    assert output is False


def test_returns_false_for_negative_numbers():

    insert = -7

    output = is_prime(insert)

    assert output is False


def test_returns_true_for_primes():

    insert = 7

    output = is_prime(insert)

    assert output is True

    insert = 61

    output = is_prime(insert)

    assert output is True

    insert = 100000007

    output = is_prime(insert)

    assert output is True
