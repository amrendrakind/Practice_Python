print("Travel from city A to city B")
time = int(input("Enter time: "))
longer = int(input("Define longer: "))
if (time > longer):
    price = int(input("Enter price: "))
    higher = int(input("Define higher: "))
    if (price >= higher):
        print("Train")
    else:
        print("Coach")
else:
    price = int(input("Enter price: "))
    higher = int(input("Define higher: "))
    if(price >= higher):
        print("Daytime flight")
    else:
        print("Red Eye flight")
print("Arrive City B")