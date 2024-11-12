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

def binary_search(L,k):
    a = time.time()
    begin = 0
    end = len(L) - 1
    while ((end-begin) > 1):
        mid = (end + begin)//2
        if(L[mid] == k):
            b = time.time()
            print(f"Time taken", (b - a))
            return 1
        if(k < L[mid]):
            end = mid - 1
        if(k > L[mid]):
            begin = mid + 1
    if(L[begin] == k) or(L[end] == k):
        b = time.time()
        print(f"Time taken", (b - a))
        return 1
    else:
        b = time.time()
        print(f"Time taken", (b - a))
        return 0

L = list(range(100000000))
k = -1
print(obvious_search(L,k))
print(binary_search(L,k))