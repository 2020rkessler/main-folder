# WARM UP
# Create a new file called 02_index.py in warmups
# Create an array of 10 random ints
# Loop through the array and print out all the
# index values
# EXAMPLE:
arr = [10,4,21,17,34,12,76,43,23,2]
# OUTPUT on first iteration:  0
# OUTPUT on second iteration: 1
# keeping tack of index value
idx = 0
for num in arr:
    print(idx)
    idx = idx + 1

if arr[2] == 21:
    print('true')
