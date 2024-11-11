first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
full_name = first_name+" "+last_name
print("Your full name is: ", full_name)

l = list(range(10))
str_concat = ''
for i in l:
    str_concat = str_concat + str(i) + ' '
print(len(str_concat))
print(str_concat.strip())
print(len(str_concat.strip()))