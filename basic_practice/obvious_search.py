import time

def obvious_search(L,k):
    a = time.time()
    for i in L:
        if i == k:
            b = time.time()
            print(f"Time taken", (b - a))
            return 1
    b = time.time()
    print(f"Time taken", (b - a))
    return 0
L = list(range(100000000))
print(obvious_search(L,9999999))