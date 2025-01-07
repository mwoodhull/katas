def duplicate_count(text):

    count = 0
    l_text = text.lower().replace(" ", "")

    for char in l_text:
        if len(l_text) - len(l_text.replace(char, "")) >= 2:
            count += 1
            l_text = l_text.replace(char, "")

    return count
