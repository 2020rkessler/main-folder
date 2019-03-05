def encrypt(string, shift):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
    number_hash = {}
    alphabet_hash = {}
    count = 1
    for x in range(len(alphabet)):
        number_hash[x+1] = alphabet[x]
    for y in alphabet:
        alphabet_hash[y] = count
        count += 1

    word = list(string)
    newword = []

    for letter in word:
        if letter in alphabet:
            position = alphabet_hash[letter]
            position += shift
            if position > 26:
                position -= 26
                newletter = number_hash[position]
                newword.append(newletter)
            else:
                newletter = number_hash[position]
                newword.append(newletter)
        else:
            newword.append(letter)

    print(''.join(newword))

encrypt("cool", 1)

def decrypt(string, shift):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    number = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
    number_hash = {}
    alphabet_hash = {}
    count = 1
    for x in range(len(alphabet)):
        number_hash[x+1] = alphabet[x]
    for y in alphabet:
        alphabet_hash[y] = count
        count += 1


    word = list(string)
    newword = []

    for letter in word:
        if letter in alphabet:
            position = alphabet_hash[letter]
            position -= shift
            if position < 0:
                position += 26
                newletter = number_hash[position]
                newword.append(newletter)
            else:
                newletter = number_hash[position]
                newword.append(newletter)
        else:
            newword.append(letter)

    print(''.join(newword))


decrypt("dppm", 1)
