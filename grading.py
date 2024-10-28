marks = -1
while (marks < 0 or marks > 100):
    marks = int(input("Enter your marks between 0 and 100: "))
    if (marks <0 or marks >100):
        print("Invalid input")
if (marks >= 90):
    print("A")
elif(marks >= 80):
    print("B")
elif(marks >= 70):
    print("C")
elif(marks >= 60):
    print("D")
else:
    print("E")