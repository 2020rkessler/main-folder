import random
def s_search(arr, num):
    # index value starts at -1, because we increase
    # on every iteration of the loop
    idx = -1
    # hold all index values
    pos_master = []
    for int in arr:
        # index value goes up by one
        idx = idx + 1
        # if iterator == searched for num
        if int == num:
            # print index value
            pos_master.append(idx)
    return pos_master

ar = [random.randint(0,10) for x in range(50)]
pos = s_search(ar, 3)
print("the number", ar[pos[0]], "is found at index(s):", pos)
