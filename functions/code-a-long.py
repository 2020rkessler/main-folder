# reading: https://www.codementor.io/kaushikpal/user-defined-functions-in-python-8s7wyc8k2

# built in functions
print('hello, I am a function')
print(len('hello'))
# user defined functions
# create a function called find_me()
# args1 = arr of ints
# arg2 = one number you are looking for
# output =  1.) true or false
#           2.) print the index value of where that int is

def find_me(arr, num):
    for val in arr:
        if val == num:
            print('True')
            return(True)
        else:
            print('False')
            return(False)
# call the method
lotto = [24,2123,123,342,345,457,345,24,234,3457,6687,2]
ans = find_me(lotto, 2)



# required and default arguments
def dog(woof, bork='borking so loud'):
    print(woof,bork)

dog('woofwoof')


# variable number of arguments
def cat(*maths):
    ans = 1
    for x in maths:
        ans = ans * x
    print(ans)
cat(10,10,10)
cat(10)
