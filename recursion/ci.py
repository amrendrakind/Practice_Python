def compound_interest(p,r,n):
    if n == 1:
        return p*(1+r/100)
    else:
        return(compound_interest(p,r,n-1)*(1+r/100))

print(compound_interest(100,10,1))
print(compound_interest(100,10,2))
print(compound_interest(100,10,3))