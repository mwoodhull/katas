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

    powers_dict = {"hundred": 100, "thousand": 1000, "million": 1000000000}

    for key in unit_dict:
        if string == key:
            return unit_dict[string]
        
    for key in teens_dict:
        if string == key:
            return teens_dict[string]
        
    for key in tens_dict:
        if string == key:
            return tens_dict[string]
        
    for key in powers_dict:
        if string == key:
            return powers_dict[string]
