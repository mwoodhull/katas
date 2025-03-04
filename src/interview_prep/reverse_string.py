def reverse(words):

    backwards = words[::-1]

    return backwards

def find_largest(nums):

    return max(nums)

import math

def is_prime(integer):
    if integer <= 1:
        return False
    
    for i in range(2, int(math.sqrt(integer)) + 1):
        if integer % i == 0:
            return False
        
    return True