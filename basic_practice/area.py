import math
PI = math.pi
def area_circle(r):
    return (PI * r * r)

def area_rectangle(l,b):
    return (l * b)

def perimeter_circle(r):
    return (2 * PI * r)

def perimeter_rectangle(l,b):
    return (2 * (l + b))

print("POLYGONS\n1.Circle\n2.Rectangle")
polygon = ''
while(polygon != 'exit'):
    polygon = str(input("Enter type of polygon or 'exit': "))
    if polygon == 'cicle' or polygon == 'Circle' or polygon == '1':
        r = float(input("Enter the radius of circle: "))
        cp = ''
        while(cp == ''):
            print("\nCIRCLE PROPERTIES\n1.Area\n2.Perimeter")
            cp = str(input("choose the circle property or go back "))
            if cp == 'area' or cp == 'Area' or cp == '1':
                area = area_circle(r)
                print(f"Area of circle with radius {r} is {area}")
                cp = ''
            elif cp == 'perimeter' or cp == 'Perimeter' or cp == '2':
                permeter = perimeter_circle(r)
                print(f"Perimeter if circle with radious {r} is {perimeter}")
                cp = ''
            elif cp == 'back':
                break
            else:
                print("Please select correct polygon type or 'exit' ")
                cp = ''
    elif polygon == 'rectangle' or polygon == 'Rectangle' or polygon == '2':
        l = float(input("Enter length of rectangle: "))
        b = float(input("Enter breadth of rectangle: "))
        rp = ''
        while(rp == ''):
            print("\nRECTANGLE PROPERTIES\n1.Area\n2.Perimeter")
            rp = str(input("choose the rectangle property or go back " ))
            if rp == 'area' or rp == 'Area' or rp == '1':
                area = area_rectangle(l,b)
                print(f"Area of rectangle with lengh {l}, breadth {b} is {area}")
                rp =''
            elif rp == 'perimeter' or rp == 'Perimeter' or rp == '2':
                perimeter = perimeter_rectangle(l,b)
                print(f"Perimeter of rectangle with lengh {l}, breadth {b} is {perimeter}")
                rp =''
            elif rp == 'back':
                break
            else:
                print("Please select correct polygon type or 'exit' ")
                rp = ''
    elif polygon == 'exit':
        break
    else:
        print("Please select correct polygon type or 'exit' ")
