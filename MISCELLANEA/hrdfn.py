"""
Higher-order functions allow re-use of control flow
"""

from numpy import pi

def area(r): return pi * r * r

def circumference(r): return 2 * pi * r

def slim(text): return text[1:-1]

def add(x, y): return x + y

def mul(x, y): return x * y

def do_all(func, values):
    result = []
    for v in values:
        temp = func(v)
        result.append(temp)
    return result

def combine_values(func, *values):
    current = 0
    if len(values) > 0:
        current = values[0]
        for i in range(1, len(values)):
            v = values[i]
            current = func(current, v)
    return current

def add_all(*args):
    total = 0
    for a in args:
        total += a
    return total

def test():
    print do_all(area, [1.0, 2.0, 3.0])
    print do_all(circumference, [1.0, 2.0, 3.0])
    print do_all(slim, ['abc', 'defgh'])
    print combine_values(add, 1, 3, 5)
    print combine_values(mul, 1, 3, 5)
    print combine_values(add)
    print add_all(1, 2, 3)
#    print add_all('ab', 'cd', 'ef')
