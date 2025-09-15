# Function
def is_even(num):
    if num%2==0:
        return'Number is even.'
    else:
        return'Number is odd.'
print(is_even(9))

# If function do not have return statements.
def is_even(num):
    if num%2==0:
        print('Number is even.')
    else:
        print('Number is odd.')
print(is_even(9)) # Along with it give that Number is odd it does not return any value so it give None too.

# Variable Scope
def g(y):
    print(x)
    print(x+1)
x=5
g(x)
print(x)
# Output: 5
#         6
#         5

def f(y):
    x=1
    x+=1
    print(x)
x=5
f(x)
print(x)
# Output: 2
#         5

# def h(y):
#    x+=1
# x=5
# h(x)
# print(x)

def h(y):
    global x
    x+=1
x=5
h(x)
print(x)
# Output: 6
