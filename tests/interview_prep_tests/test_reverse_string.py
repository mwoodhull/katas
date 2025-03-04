from src.interview_prep.reverse_string import reverse
from src.interview_prep.reverse_string import find_largest
from src.interview_prep.reverse_string import is_prime


def test_returns_reversed_string():

    insert = 'hello'

    output = reverse(insert)

    assert output == 'olleh'

def test_find_largest_works():

    insert = [4, 6, 9, 11, 2]

    output = find_largest(insert)

    assert output == 11

def test_finding_prime():

    insert = 6
    output = is_prime(insert)

    assert output is False

    insert = 7
    output = is_prime(insert)

    assert output is True