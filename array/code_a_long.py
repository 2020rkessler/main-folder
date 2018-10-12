# Arrays are cool
# Created an array
arr = ['Estelle', 'Ben', 'Lauren', 'Patches', 'Kyle', "meow"]
# how do indexes work?
# access last element
print("I am the last element", arr[-1])
# access the first element
print("I am the first element", arr[0])
# get len of Array
print("I have", len(arr), "elements in me")
# pop to remove last element
arr.pop()
print(arr)
# remove a certain element
arr.remove('Kyle')
print(arr)
# add something to an array
arr.append('Woof')
print(arr)

# For loop
for name in arr:
    print(name)

# While loop
count = 0
while len(arr) < count:
    print(count)
    count = count + 1

arr2 = ['bork', 'boof', 'foobar', 'fish']

arr3 = arr + arr2
print(arr3)

# For loop
for name in arr3:
    print(name)

# add to array
arr3.append('add me')
print(arr3)


arr = ['kyle', 'lauren', 'estelle', 'ben']

for names in arr:
    # turn str into arr
    name_change = list(names)
    # cap the first letter
    name
