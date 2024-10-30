number = int(input("Enter a number "))
abs_number = abs(number)
reverse_number = abs_number % 10
abs_number = abs_number // 10
while (abs_number > 0):
    reverse_number = reverse_number * 10 + abs_number % 10
    abs_number = abs_number // 10
if(number < 0):
    reverse_number = reverse_number*-1
if (number == reverse_number):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
