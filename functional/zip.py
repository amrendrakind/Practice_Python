fruits = ["Mango", "Apple", "Banana", "Orange", "Pineaple", "Watermelon", "Guava", "Kiwi"]
size = [5,5,6,6,9,10,5,4]
d = dict(zip(fruits,size))
print(d)
print(list(zip(fruits,size)))
z = zip(fruits,size)
print(next(z))
for i in z:
    print(i)

for k in d:
    print(d[k])