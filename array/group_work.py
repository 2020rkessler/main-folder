import random
# 1.) create an array of names
names = ['Estelle', 'Ben', 'Woof', 'Bork']
# 2.) use the append method to add a new name
names.append('Doggo')
# 3.) remove the item at index 2
names.remove('Woof')
# 3.) add an item to the last index
names.append('Doggo')
# 4.) create a second array of names
names2 = ['Kyle', 'Lauren', 'Jamesers', 'Erin', 'Izzy', 'Optimus prime']
# 5.) add the two arrays together in a new array
all_names = names + names2
print(all_names)
# 6.) using a for loop, print out all the names from the array
for name in all_names:
    print(name)
# 7.) using a for loop and string interpolation create a
#     party invite for all names in the list
for name in all_names:
    print("Hello ", name, "you have a ticket to the best party ever")
# 8.) using a for loop with an if/else, print a unique
#    message for names that start with a vowel vs. names that don't
vowels = ['a','e','i','o','u','A','E','I','O','U']
for name in all_names:
    if name[0] in vowels:
        print(name, "starts with a vowel")
    else:
        print(name, "does not start with a vowel")

# Mild Challenge

# 1.) create an array of ints
ints = [random.randint(0,10) for x in range(10)]
# 2.) using a for loop and branching, return only the even nums
for num in ints:
    if num % 2 == 0:
        print(num, 'Is Even')
    else:
        print(num, 'Is Odd')

# Spicy Challenge of the week
# 1.) create an array of names all in lowercase
lowercase = ['ben', 'estelle', 'lauren', 'meow']
uppercase = []
# 2.) Using a loop and indexes, capitalize the first letter of each name
count = 0
for name in lowercase:
    # turn x into list
    name = list(name)
    # turn first letter into cap
    name[0] = name[0].upper()
    # turn list into str
    name = "".join(name)
    # add to array upper
    uppercase.append(name)
    lowercase[count] = name
    count = count + 1

print(uppercase)
print(lowercase)

# OR
lowercase = ['ben', 'estelle', 'lauren', 'meow']
count = 0
 for name in lowercase:
    # change name to arr
	name_change = list(name)
    # cap first letter
	name_change[0] = name_change[0].upper()
    # turn arr into str
	name_change = "".join(name_change)
    # replace value in lowercase with name_change
	lowercase[count] = name_change
    # increment for index pos
	count = count + 1
print(lowercase)

# Spicy Challenge of the Month
# You will be given an array of integers whose elements have
# both a negative
# and a positive value, except for one integer that is either only negative
# or only positive. Your task will be to find that integer.
# Input                         Output
# arr0 = [1]					#  1
# arr1 = [1,-1,2,-2,3] 			#  3
# arr2 = [-3,1,2,3,-1,-4,-2]	# -4
# arr3 = [1,-1,2,-2,3,3]		#  3
