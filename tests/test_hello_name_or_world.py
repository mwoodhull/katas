from src.hello_name_or_world import hello


def test_returns_hello_name_where_name_is_provided():

    entry = "Matthew"
    output = hello(entry)

    assert output == "Hello, Matthew!"


def test_returns_name_with_name_capitalised_where_not_already_provided():

    entry = "matthew"
    output = hello(entry)

    assert output == "Hello, Matthew!"


def test_returns_name_with_capitalised_first_letter_only_where_all_cap():

    entry = "mATTHEW"
    output = hello(entry)

    assert output == "Hello, Matthew!"


def test_returns_hello_world_where_name_is_empty_string():

    entry = ""
    output = hello(entry)

    assert output == "Hello, World!"


def test_returns_hello_world_where_wrong_data_type():

    entry = 66
    output = hello(entry)

    assert output == "Hello, World!"

    entry = True
    output = hello(entry)

    assert output == "Hello, World!"


def test_returns_hello_world_where_no_argument_provided():

    output = hello()

    assert output == "Hello, World!"
