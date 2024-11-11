def check_zero(l):
    if(len(l) == 0):
        return False
    if (l[0] == 0):
        return True
    else:
        return check_zero(l[1:len(l)])

l = [3,4,6,1,7,2,8]
print(check_zero(l))