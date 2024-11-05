import random
l = []
a = int(input("Enter a number "))
flag = 0
for i in range(100):
    l.append(random.randint(1,1000000))
print(l)
for i in range(len(l)):
    if ( a == l[i] ):
        flag = 1
        print("Hip hip hurrey, Number found")
        break
if (flag == 0 ):
    print("Number not found")
