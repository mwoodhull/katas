import string


def is_pangram(st):

    st_sorted = set(st.lower())

    filtered_letters = set()

    for letter in st_sorted:
        if letter.isalpha():
            filtered_letters.add(letter)

    ascii_set = set(string.ascii_lowercase)

    if ascii_set == filtered_letters:
        return True

    else:

        return False
