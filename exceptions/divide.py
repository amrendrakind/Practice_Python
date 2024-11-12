try:
    a = int(input("Enter a number A "))
    b = int(input("Enter a number B "))
    f = open('abc.txt','r')
    c = a / b
    print("A/B is ",c)
except ZeroDivisionError:
    print('Invalid input, divisor can not be zero.')
except ValueError:
    print("Please input number. Non-numeric input is not allowed.")
except FileNotFoundError:
    print("File not found")
except:
    print("Something went wrong!")
finally:
    try:
        f.close()
    except NameError:
        pass
    print("From finally block")