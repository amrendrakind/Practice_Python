marks = -1
while (marks < 0 or marks > 100):
    marks = int(input("Enter your marks between 0 and 100: "))
    if (marks <0 or marks >100):
        print("Invalid input")
if (marks >= 90):
    print("A")
elif(marks >= 80 and marks <90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
elif(marks >= 60 and marks < 70):
    print("D")
elif(marks < 60):
    print("E")