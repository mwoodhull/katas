from src.spin_words import spin_words


def test_returns_string_where_all_under_5_letters():

    insert = "hi this is a test"

    output = spin_words(insert)

    assert output == "hi this is a test"


def test_returns_flipped_single_word():

    insert = "hello"

    output = spin_words(insert)

    assert output == "olleh"


def test_returns_flipped_words_in_sentence_of_long_words():

    insert = "hello fantastic meeting everyone"

    output = spin_words(insert)

    assert output == "olleh citsatnaf gniteem enoyreve"


def test_returns_mix_of_flipped_words_for_varied_sentence():

    insert = "hello my name is matthew"

    output = spin_words(insert)

    assert output == "olleh my name is wehttam"
