def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y


def expo(base, power):
    return base ** power
