from src.filter_list import filter_list


def test_returns_identical_list_when_all_are_integers():

    insert = [1, 2, 3]

    output = filter_list(insert)

    assert output == [1, 2, 3]


def test_returns_new_list():

    insert = [1, 2, 3]

    output = filter_list(insert)

    assert output == [1, 2, 3]
    assert output is not insert


def test_returns_empty_list_where_all_strings():

    insert = ["a", "b", "c"]

    output = filter_list(insert)

    assert output == []


def test_returns_only_numbers_where_mix_of_data_types():

    insert = ["a", 1, 6, 3, 1.4, [1], "b"]

    output = filter_list(insert)

    assert output == [1, 6, 3]
