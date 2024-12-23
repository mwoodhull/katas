def high_and_low(numbers):

    lst = numbers.split()

    int_list = [int(i) for i in lst]

    num_string = str(max(int_list)) + " " + str(min(int_list))

    return num_string
