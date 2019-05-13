def path_finder(matrix):

    matrix = list(map(list, matrix.splitlines()))
    #converts matrix val to str
    length = len(matrix)

    start = (0,0)
#tuple
    finish = (length - 1,length - 1)


    level = {start: 0}
    parent = {start: 0}
    i = 1
    #memoization and keeps search algorithm going
    border = [start]

    while border:
        next = []
        #creates empty arr
        for u in border:
        #u = coordinate

            x,y = u
#extracting coordinate from the tuple (data structure)
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
            #cardinal directions

                if 0 <= x < length and 0 <= y < length:
                #to avoid out of range index

                    if (x,y) not in level and matrix[x][y] != 'W':
                    #if stuck, at wall
                    #checks out each node


                        parent[(x,y)] = u
                        #parent -- dictionary: allows you to retrace the path you took
                        level[(x,y)] = i
                        next.append((x,y))



                        if (x,y) == finish:
                            return True

        #list of past nodes
        border = next
        i += 1
        #keeps going
    return False

#print failed mazes
