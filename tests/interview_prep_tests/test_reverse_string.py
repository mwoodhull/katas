from src.interview_prep.reverse_string import reverse


def test_returns_reversed_string():

    insert = 'hello'

    output = reverse(insert)

    assert output == 'olleh'