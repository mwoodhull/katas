def no_boring_zeroes(num):
    
    if str(0) in str(num)[-1:] and len(str(num)) > 1:
        new_num = int(str(num)[:-1])
        return new_num
    
    else:
        return num