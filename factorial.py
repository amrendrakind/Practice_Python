n = int(input("Enter number: "))
fact = 1
num = n
while (n > 0):
    fact *= n
    n -= 1
if (n >= 0):
    print("Factorials of",num,"is",fact)
else:
    print("Not defined")