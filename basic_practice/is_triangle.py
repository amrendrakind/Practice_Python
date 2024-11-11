x1 = float(input("Enter X co-ordinate of 1st point "))
y1 = float(input("Enter Y co-ordinate of 1st point "))
x2 = float(input("Enter X co-ordinate of 2nd point "))
y2 = float(input("Enter Y co-ordinate of 2nd point "))
x3 = float(input("Enter X co-ordinate of 3rd point "))
y3 = float(input("Enter Y co-ordinate of 3rd point "))

def distance(xi,yi,xj,yj):
    return ((((xj - xi)**2) + ((yj - yi)**2))**0.5)

def isTriangle(d1,d2,d3):
    max = 0.0
    a = 0.0
    b = 0.0
    if(d1 > d2):
        if(d1 > d3):
            max = d1
            a = d2
            b = d3
        else:
            max = d3
            a = d1
            b = d2
    elif(d2 > d3):
        max = d2
        a = d1
        b = d3
    else:
        max = d3
        a = d1
        b = d2
    if((a + b) > max):
        return "Triangle"
    else:
        return "Not a triangle"


d1 = distance(x1,y1,x2,y2)
print(f"Distance between points({x1}, {y1} and {x2}, {y2}) is {d1}")

d2 = distance(x2,y2,x3,y3)
print(f"Distance between points({x2}, {y2} and {x3}, {y3}) is {d2}")

d3 = distance(x3,y3,x1,y1)
print(f"Distance between points({x3}, {y3} and {x1}, {y1}) is {d3}")
print(isTriangle(d1,d2,d3))
