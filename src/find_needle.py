def find_needle(haystack):

    needle_count = 0

    for hay in haystack:
        if hay == "needle":
            needle_count += 1
            return f"Found the needle at position {haystack.index(hay)}"

    if needle_count == 0:
        return "There are no needles!"
