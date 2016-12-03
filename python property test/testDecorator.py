def logger(func):
    def inner(*args, **kvargs):
        print "logged"
        return func(*args, **kvargs)

    return inner

def square(func):
    def inner(*args, **kvargs):
        total = func(*args, **kvargs)
        return total * total
    return inner

# @logger
# @square
def sum(a, b):
    return (a + b)

# Decorator equals to the following funcs
sumSquare = square(sum)
result = logger(sumSquare)
print result(1, 2)
