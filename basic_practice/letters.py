
def upper_case(sentence):
    upper_count = 0
    for c in sentence:
        if c.isupper():
            upper_count += 1
    return upper_count

def lower_case(sentence):
    lower_count = 0
    for c in sentence:
        if c.islower():
            lower_count += 1
    return lower_count

def total_no_of_char(sentence):
    no_of_char = 0
    for c in sentence:
        no_of_char += 1
    return no_of_char

def total_no_of_words(sentence):
    if len(sentence) > 0:
        word_count = 1
    else:
        word_count = 0
    for c in sentence:
        if c == ' ':
            word_count += 1
    return word_count

# sentence = 'Functions could have no parameters'
# sentence = 'Functions Could Have Multiple Return Statements, But The Moment The First Return Is Executed, Control Exits From The Function'
# sentence = 'FUNCTIONS have to be Defined before THEY can be called. the function Call Cannot come before the DEFINITION'
# sentence = 'fUNCTION CALLS COULD BE USED IN EXPRESSIONS'
sentence = str(input("Enter sentence: "))
print(upper_case(sentence), end=" ")
print(lower_case(sentence), end=" ")
print(total_no_of_char(sentence), end=" ")
print(total_no_of_words(sentence))
