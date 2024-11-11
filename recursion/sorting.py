def minimum(l):
    m = l[0]
    for x in l:
        if x < m:
            m = x
    return m

def sort(l):
    if len(l) <= 1:
        return l
    m = minimum(l)
    l.remove(m)
    return [m] + sort(l)

l = [4,6,2,3,9,7,1]
print(sort(l))