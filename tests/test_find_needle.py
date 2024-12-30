from src.find_needle import find_needle

def test_can_return_message_where_haystack_is_all_needle():

    insert = ['needle']

    output = find_needle(insert)

    assert output == "Found the needle at position 0"

def test_can_return_message_where_needle_is_in_haystack():

    insert = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] 

    output = find_needle(insert)

    assert output == "Found the needle at position 5"

    insert = ["hayyyy", "junk", "needle", "hay", "moreJunk", "stack", "randomJunk"] 

    output = find_needle(insert)

    assert output == "Found the needle at position 2"

def test_can_return_error_message_where_there_are_no_needles():

    insert = ["hayyyy", "junk", "hay", "moreJunk", "stack", "randomJunk"] 

    output = find_needle(insert)

    assert output == 'There are no needles!'