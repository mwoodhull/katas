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

    string_lst = string.replace('-', ' ').split()
    num_lst = []


    for num in string_lst:
        if num in unit_dict:
            num_lst.append(unit_dict[num])
        elif num in teens_dict:
            num_lst.append(teens_dict[num])
        elif num in tens_dict:
            num_lst.append(tens_dict[num])
        elif num in powers_dict:
            num_lst.append(powers_dict[num])
            
    if len(num_lst) == 1:
        return num_lst[0]
    
    if 2 <= len(num_lst) < 4:
        return sum(num_lst)
        
    if len(num_lst) < 5:
        num_lst[0:2] = [num_lst[0] * num_lst[1]]
        return sum(num_lst)
    
    if len(num_lst) < 6:
        num_lst[1:3] = [num_lst[1] * num_lst[2]]
        return sum(num_lst)
    
    if len(num_lst) < 7:
        num_lst[0:2] = [num_lst[0] * num_lst[1]]
        num_lst[1:3] = [num_lst[1] * num_lst[2]]
        return sum(num_lst)
        
