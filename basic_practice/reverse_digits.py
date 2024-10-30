num = int(input("Enter a number: "))
abs_number = abs(num)
reverse_number = abs_number % 10
abs_number = abs_number // 10
while (abs_number > 0):
    reverse_number = reverse_number*10 + abs_number % 10
    abs_number = abs_number // 10
if(num > 0):
    print("Reverse number is ", reverse_number)
else:
    print("Reverse Number is ", reverse_number*-1)
