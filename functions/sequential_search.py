import random

arr2 = []
for x in range(1000):
    arr2.append(random.randint(0,100))

def sq_search(arr, num):
    count = -1
    for x in arr:
        count = count + 1
        if x == num:
            print(count)
            return count
            break

sq_search(arr2, 8)
my_num = sq_search(arr2, 10)
print(my_num)
print(arr2[my_num])
