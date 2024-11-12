import math
a = [25, 16, -9, 81, -100]

def sqroot(x):
    return math.sqrt(x)

def is_positive(n):
    if n>=0:
        return n

root = map(sqroot, filter(is_positive, a))
print(list(root))