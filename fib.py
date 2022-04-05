# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(99999999999999999)



# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(99999999999999999):
    print(i)

