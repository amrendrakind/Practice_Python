alpha = 'abcdefghijklpmnopqrstuvwxyz'
s='amrendra'
length = len(s)
i = 0
k = 3
t=''
while(i<length):
    t=t+(alpha[(((alpha.index(s[i]))+k)%26)])
    i+=1
print(t)