fruits = ["Mango", "Apple", "Banana", "Orange", "Pineaple", "Watermelon", "Guava", "Kiwi"]
basket = iter(fruits)
print(basket)
print(next(basket))
print(next(basket))
print(next(basket))
print(next(basket))
print(next(basket))

for fruit in basket:
    print(fruit)