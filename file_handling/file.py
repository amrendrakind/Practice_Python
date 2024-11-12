f = open('newfile.txt', 'w')

f.write('Hello!!!\n')
f.write("Amrendra ")
f.write('KUmar')
f.close()
f = open('newfile.txt', 'r')
s = f.read()
print(s)