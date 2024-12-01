def no_of_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + no_of_digits(n//10)

print(no_of_digits(456123789))
