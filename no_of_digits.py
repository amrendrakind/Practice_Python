number = int(input("Enter a number: "))
num = number
digits = 1
while (number > 9):
    number = number//10
    digits += 1
print("Number of digits in",num, "is", digits )