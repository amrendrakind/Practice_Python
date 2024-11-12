try:
    a = int(input("Enter a number A "))
    b = int(input("Enter a number B "))
    c = a / b
    print(f"A/B is ",c)
except ZeroDivisionError:
    print('Invalid input, divisor can not be zero.')
except ValueError:
    print("Please input number. Non-numeric input is not allowed.")