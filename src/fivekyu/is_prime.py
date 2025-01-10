def is_prime(num):

    for integer in range(2, num):
        if num % integer == 0:
            return False

    if num % 2 == 0 and num != 2 or num < 2:
        return False

    else:

        return True
