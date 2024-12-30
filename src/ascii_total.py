def uni_total(character):

    char_list = list(character)
    ascii_total = 0

    for cha in char_list:
        ascii_total += ord(cha)
    
    return ascii_total