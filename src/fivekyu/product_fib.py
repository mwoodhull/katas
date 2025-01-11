"""creates list of fibonacci sequence
    n = the length of the sequence to be provided """


def fibonacci(n):

    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


"""takes prod as an argument and finds whether two numbers next
    to each other in the fibonacci sequence multiply together
    to create the product argument
    
    if not, it will return the last two numbers which multiply
    to give a number less than the product argument"""


def product_fib(prod):

    total = 0
    fib_list = fibonacci(1000)

    for i in range(len(fib_list) - 1):
        total = fib_list[i] * fib_list[i + 1]
        if total == prod:
            return [fib_list[i], fib_list[i + 1], True]

        elif total > prod:
            return [fib_list[i], fib_list[i + 1], False]

    return total


print(product_fib(1001))
