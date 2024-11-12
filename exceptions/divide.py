a = int(input("Enter a number A "))
b = int(input("Enter a number B "))
try:
    c = a / b
    print(f"A/B is ",c)
except ZeroDivisionError:
    print('Invalid input, divisor can not be zero')
