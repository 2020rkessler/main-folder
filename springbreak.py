import string
import numpy as np

#arrayay stores the keyboard characters in each line
line1 = ["q","w","e","r","t","y","u","i","o","p"]
line2 = ["a","s","d","f","g","h","j","k","l"]
line3 = ["z","x","c","v","b","n","m",",","."]

def shift_encryption(index, shift, array):
    #find character shift
    total_shift = int(index) + int(shift)
    #check the boundaries of the shift to make sure it is still within
    if total_shift  > len(array)-1:
        #change the shift value if total_shift is > len of array -1
        total_shift = total_shift - len(array)
    #get the new index value of shifted
    shifted = array[total_shift]
    return shifted


def shift_decyrpt(index, shift, array):
    #find total shift
    total_shift = int(index) - int(shift)
    #check boundaries of shift
    if total_shift < 0:
        #if total_shift is < 0 adjust shift_val
        total_shift = total_shift + len(array)
    #get the new index value of shifted
    shifted = array[total_shift]
    return shifted


def encrypt(text, encryptkey):
    #clear array for output
    output = ""

    special_characters = {",":"<", ".":">"}

    #convert shift_val into string
    encryptkey = str(encryptkey)

    if len(encryptkey) == 1:
        encryptkey += encryptkey[0]
        encryptkey += encryptkey[0]
    #get shift values for each line from input
    line_1_shift = encryptkey[0]
    line_2_shift = encryptkey[1]
    line_3_shift = encryptkey[2]

    #loop through each character
    for character in text:
        #if character is space append to encrypted
        if character == " ":
            output += " "
            continue
        #keep track of upp and low
        if character.islower() or character in special_characters.keys():
            is_lower = True
        elif not character.islower():
            if character in special_characters.values():
                #retrieve key of special_characters array from val
                character = list(special_characters.keys())[list(special_characters.values()).index(character)]
            is_lower = False
            character = str.lower(character)
        #find character line and index
        if character in line1:
            index = line1.index(character)
            shifted = shift_encryption(index, line_1_shift, line1)
        elif character in line2:
            index = line2.index(character)
            shifted = shift_encryption(index, line_2_shift, line2)
        elif character in line3:
            index = line3.index(character)
            shifted = shift_encryption(index, line_3_shift, line3)
        else:
            shifted = character

        if not is_lower:
            #fix lower and upper
            if shifted in special_characters.keys():
                shifted = special_characters.get(shifted)
            shifted = str.upper(shifted)
        output +=(shifted)
    return output

def decrypt(text, encryptkey):
    #empty array to store output
    output = ""

    special_characters = {",":"<", ".":">"}

    #convert shit to str
    encryptkey = str(encryptkey)

    if len(encryptkey) == 1:
        encryptkey += encryptkey[0]
        encryptkey += encryptkey[0]
    #retrieve shift_val
    line_1_shift = encryptkey[0]
    line_2_shift = encryptkey[1]
    line_3_shift = encryptkey[2]

    #loop through each character
    for character in text:
        #if character is space append to encrypted
        if character == " ":
            output += " "
            continue
        #keep track of upper or lower
        if character.islower() or character in special_characters.keys():
            is_lower = True
        elif not character.islower():
            if character in special_characters.values():
                #obtain key of special_characters
                character = list(special_characters.keys())[list(special_characters.values()).index(character)]
            is_lower = False
            character = str.lower(character)
        #find line, index, and then shift
        if character in line1:
            index = line1.index(character)
            shifted = shift_decyrpt(index, line_1_shift, line1)
        elif character in line2:
            index = line2.index(character)
            shifted = shift_decyrpt(index, line_2_shift, line2)
        elif character in line3:
            index = line3.index(character)
            shifted = shift_decyrpt(index, line_3_shift, line3)
        else:
            shifted = character

        if not is_lower:
            #fix lower and upper
            if shifted in special_characters.keys():
                shifted = special_characters.get(shifted)
            shifted = str.upper(shifted)
        output +=(shifted)
    return output
