maxLen = 0
word= ''
while(word != '-1'):
    word = str(input("Enter a word "))
    count = 0
    for c in word:
        count += 1
    if (count > maxLen):
        maxLen = count
print('The length of longest word is %s' %maxLen)
