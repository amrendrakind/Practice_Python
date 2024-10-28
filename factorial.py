n = int(input("Enter number: "))
fact = 1
while (n > 0):
    fact *= n
    n -= 1
print("Factorials of",n,"is",fact)