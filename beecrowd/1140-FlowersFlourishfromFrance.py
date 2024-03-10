# check if is tautogram
# I should do this using functions

while True:
    sentence = input()
    msg = 'N'
    if sentence == '*':
        break
    b = sentence.split()
    first_letter = b[0][0]
    for word in b:
        if word[0].lower() == first_letter.lower():    
            msg = 'Y'
        else:
            msg = 'N'
            break
    print(msg)
