def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))