import string

def is_pangram(st):

    st_sorted = sorted(set(st.lower()))

    filtered_letters = set()

    for letter in st_sorted:
        if letter.isalpha():
            filtered_letters.add(letter)
    print(filtered_letters)

    ascii_set = sorted(set(string.ascii_lowercase))
    print(ascii_set)

    if ascii_set == filtered_letters:
        return True
    
    else:

        return False