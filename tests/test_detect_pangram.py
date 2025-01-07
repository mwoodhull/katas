from src.detect_pangram import is_pangram


def test_returns_false_when_empty_string():

    insert = ""

    output = is_pangram(insert)

    assert output == False


def test_returns_true_for_lower_case_pangram_letters_only():

    insert = "thequickbrownfoxjumpsoverthelazydog"

    output = is_pangram(insert)

    assert output == True


def test_returns_true_for_pangram_with_spaces_and_uppercase():

    insert = "The quick brown fox jumps over the lazy dog"

    output = is_pangram(insert)

    assert output == True


def test_returns_false_where_not_pangram():

    insert = "Matt is new to coding"

    output = is_pangram(insert)

    assert output == False


def test_can_handle_all_sorts_of_characters():

    insert = "The435324 quick brown!!££ fox jumps68 over ...|!!the lazy dog"

    output = is_pangram(insert)

    assert output == True
