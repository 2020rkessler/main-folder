#Take the value and index as inputs, and then, in return, have the output be the value of the "piece" at the reversed index
#Hint: "pieces" are numbered sequentially from the first index

def reverse_piece(value, piece_index):
    b = bin(value)[2:]
    if piece_index > len(b): b = b.zfill(piece_index)
    index, b = len(b) - piece_index, list(b)
    b[index] = '1' if b[index] == '0' else '0'
    return int(''.join(b), 2)

print(reverse_piece(19,7))

#in order to check if your solution is correct, when calling the function, if the inputs are 19,7 (the replacement for their named counterparts (replacing value, piece_index)), then the output should be 83.
