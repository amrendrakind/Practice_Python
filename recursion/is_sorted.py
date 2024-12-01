def is_sorted(a, size):
    if size <= 1:
        return True

    if a[0] > a[1]:
        return False
    else:
        return is_sorted(a[1:], size-1)

n = [1,2,3,0] 
print(is_sorted(n, len(n)))