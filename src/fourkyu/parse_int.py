def parse_int(string):

    unit_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    teens_dict = {
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
    }

    tens_dict = {
        "ten": 10,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }

    powers_dict = {"hundred": 100, "thousand": 1000, "million": 1000000}

    string_lst = string.replace("-", " ").split()
    current_total = 0
    final_total = 0

    for num in string_lst:
        if num in unit_dict:

            current_total += unit_dict[num]
        elif num in teens_dict:

            current_total += teens_dict[num]
        elif num in tens_dict:

            current_total += tens_dict[num]
        elif num in powers_dict:

            if powers_dict[num] == 100 and current_total == 0:
                current_total += 100
            elif powers_dict[num] == 100 and current_total != 0:
                current_total *= 100
            elif powers_dict[num] != 100 and current_total == 0:
                current_total += powers_dict[num]
            else:
                current_total *= powers_dict[num]
                final_total += current_total
                current_total = 0

    final_total += current_total
    return final_total
