# Nested Functions
def f():
    def g():
        print('Inside function g')
    g()
    print('Inside function f')
f()
# Output: Inside function g
#         Inside function f

def g(x):
    def h():
        x='abc'
    x=x+1
    print('in g(x):x=',x)
    h()
    return x
x=3
x=g(x)
# Output: in g(x):x= 4

def g(x):
    def h(x):
        x=x+1
        print("in h(x):x=",x)
    x=x+1
    print('in g(x):x=',x)
    h(x)
    return x
x=3
z=g(x)
print('in main program scope:x=',x)
print('in main program scope:z=',z)

# Output: in g(x):x= 4
#         in h(x):x= 5
#         in main program scope:x= 3
#         in main program scope:z= 4

# Function are first class citizen.

# type and id
def square(num):
    return num**2
print(type(square))
a=2
print(id(a))
print(id(square))
# Output: <class 'function'>
#         140713731639768
#         2456012560864

# reassign
x=square
print(id(x))
# Output: 140713731639768


# deleting a function
# We can delete a function using del function with function name.

# storting
l=[1,2,3,4,5,square]
print(l[-1](3))
# Output: 9

# returning a function
def f():
    def x(a,b):
        return a+b
    return x
val=f()(3,4)
print(val)
# Output: 7
