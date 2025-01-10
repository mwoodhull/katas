from src.duplicate_count import duplicate_count


def test_returns_zero_where_no_duplicates():

    insert = "abcdef"

    output = duplicate_count(insert)

    assert output == 0


def test_counts_two_letters_that_appear_twice():

    insert = "ibib"

    output = duplicate_count(insert)

    assert output == 2


def test_counts_all_characters_including_numbers():

    insert = "123123123"

    output = duplicate_count(insert)

    assert output == 3


def test_can_ignore_different_cases():

    insert = "AbCaBcAbCabcABCABC"

    output = duplicate_count(insert)

    assert output == 3

    insert = "AabB"

    output = duplicate_count(insert)

    assert output == 2


def test_can_handle_spaces():

    insert = "a b c a b c"

    output = duplicate_count(insert)

    assert output == 3
