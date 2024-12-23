from src.no_boring_zeroes import no_boring_zeroes

def test_number_with_no_zero_returns_same_number():

    entry = 123

    output = no_boring_zeroes(entry)

    assert output == 123

def test_number_with_single_zero_at_end_removes_it():

    entry = 1230

    output = no_boring_zeroes(entry)

    assert output == 123

def test_only_zero_at_end_of_number_is_removed():

    entry = 1023
    output = no_boring_zeroes(entry)

    assert output == 1023

    entry = 10002300000
    output = no_boring_zeroes(entry)

    assert output == 1000230000

def test_lone_zero_returns_zero():

    entry = 0
    output = no_boring_zeroes(entry)

    assert output == 0

    entry = 1
    output = no_boring_zeroes(entry)

    assert output == 1
