names = ['kyle', 'erin', 'estelle', 'ben']
backwards = []
pos = 0

# First reverse
# len() returns how long an array is
while pos < len(names):
    last = names.pop()
    backwards.append(last)

print(names)
print('I am backwards',backwards)
