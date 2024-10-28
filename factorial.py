n = int(input("Enter number: "))
fact = 1
num = n
if (n < 0):
    print("Not defined")
else:
    while (n > 0):
        fact *= n
        n -= 1
    print("Factorials of",num,"is",fact)
