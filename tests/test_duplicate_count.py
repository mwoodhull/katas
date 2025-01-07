from src.duplicate_count import duplicate_count

def test_returns_zero_where_no_duplicates():

    insert = 'abcdef'

    output = duplicate_count(insert)

    assert output == 0