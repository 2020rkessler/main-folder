def convert_value (number):
    hexadecimal = ""
    original_number = number

    #while the remainder is not 0
    while number != 0:
        #get the remaineder of the input number devided by 16
        remainder = number%16

        #if the remained is not 1-9, get its corrosponding hexadecimal value
        if remainder == 10:
            remainder = "A"
        elif remainder == 11:
            remainder = "B"
        elif remainder == 12:
            remainder = "C"
        elif remainder == 13:
            remainder = "D"
        elif remainder == 14:
            remainder = "E"
        elif remainder == 15:
            remainder = "F"

        #convert to string
        hexadecimal += str(remainder)

        #devide number by 16 and restart the process
        number = int(number/16)

    #if the number is a single digit number, add a 0 infront
    if len(str(original_number)) == 1:
        hexadecimal += "0"

    #convert hexadecimal to list
    hexadecimal = list(hexadecimal)
    #not sure why, but the hexadecimal value is always reversed so simply reverse the list
    old_first_val = hexadecimal[0]
    hexadecimal[0] = hexadecimal[-1]
    hexadecimal[-1] = old_first_val
    #convert back to string
    hexadecimal = "".join(hexadecimal)
    return hexadecimal

def rgb (r,g,b):
    #round all values to 255 if above 255 and to 0 if below 0
    if r > 255:
        r = 255
    elif r < 0:
        r = 0

    if g > 255:
        g = 255
    elif g < 0:
        g = 0

    if b > 255:
        b = 255
    elif b < 0:
        b = 0

    #convert each value to its hexadecimal form
    r = convert_value(r)
    g = convert_value(g)
    b = convert_value(b)

    return r + g + b
