number = int(input("Enter number: "))
if (number % 5 == 0):
    if (number % 10 == 0):
        print(0)
    else:
        print(5)
else:
    print("Other")