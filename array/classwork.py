arr = ['kyle', 'lauren', 'estelle', 'ben']
# loop through every item
uppercase = []
count = 0
for name in arr:
    # turn str into array
    name_change = list(name) # 'kyle' => ['k','y','l','e']
    # turn first letter to upper
    name_change[0] = name_change[0].upper() # name_change[0] => ['K']
    # turn array into str using
    name_change = ''.join(name_change)
    # arr[name] = name_change
    # TypeError: list indices must be integers or slices, not str
    # how do I keep track on my index values as I loop?
    arr[count] = name_change
    count = count + 1
print(arr)
# First reverse
# Reverse the array
# pos = 0
# backwards = []
# while pos < len(arr):
#    last = arr.pop()
#    backwards.append(last)
# print(backwards)
