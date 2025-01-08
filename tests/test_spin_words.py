from src.spin_words import spin_words

def test_returns_string_where_all_under_5_letters():

    insert = "hi this is a test"

    output = spin_words(insert)

    assert output == 'hi this is a test'