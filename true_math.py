from math import inf


def divide(first, second):
    try:
        return first/second
    except ZeroDivisionError:
        return inf