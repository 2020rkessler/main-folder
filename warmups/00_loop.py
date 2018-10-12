arr = ['kyle', 'estelle', 'ben', 'meow']
# keeps track of index value
pos = 0
# cap every word in arr
for name in arr:
    # takes name redifines it in upper
    name = name.upper()
    # redefine each index value as name
    arr[pos] = name
    # moves the index value up
    pos = pos + 1
print(arr)
