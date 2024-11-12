a = [10,20,30,40,50,60]
b = [5,10,15,20,25,30]

def sub(x,y):
    return (x-y)

def increment(x):
    return (x+1)
m = map(sub,a,b)
inc = map(increment,a)
print(list(m))
print(list(inc))