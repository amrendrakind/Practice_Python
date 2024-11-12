def binary_search(L, k, begin, end):
    if(begin==end):
        if(L[begin] == k):
            return 1
        else:
            return 0
    if(end - begin == 1):
        if(L[begin] == k or L[end] == k):
            return 1
        else:
            return 0
    if(end - begin > 1):
        mid = (begin+end)//2
        if(L[mid] == k):
            return 1
        if(L[mid] < k):
            begin = mid + 1
        if(L[mid] > k):
            end = mid -1
    if (end - begin < 0):
        return 0
    return binary_search(L, k, begin, end)
begin = 0
end = 1000000
L = list(range(end))
k = -1
print(binary_search(L,k,0,end-1))