
# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
memory = {}


def memoize_factorial(f):
    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(99999))