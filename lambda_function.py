# Advance lambda Function.
# map function syntax
# map(<function><user define and in built function>,<iterable>)

# map
number_list=[1,11,111,1111]
square_number_list=list(map(lambda num:num**2,number_list))
print("Output:")
print("Square of number_list", square_number_list)

# Simple example
temp=input("Enter two numbers seperated by comma").split(',')
a,b = map(int,temp)
print(b)

# Simple example
temp=input("Enter two numbers seperated by comma").split(',')
b = list(map(int,temp))
print(b)

# filter function
# filter() syntax
# filter(some_function,iterable)
number_list=[1,5,67,34,68,9]
even_number_list=tuple(filter(lambda num:num%2==0, number_list))
print("Output:")
print("The even number list are: ",even_number_list)

number_list=[1,5,67,34,68,9]
even_number_list=set(filter(lambda num:num%2==0, number_list))
print("Output:")
print("The even number list are: ",even_number_list)

# filter out the value which is less than 20 and divisible by 3.
number_list=[1,5,67,34,68,9,21,27]
even_number_list=list(filter(lambda num:num>20 and num%3==0, number_list))
print("Output:")
print("The even number list are: ",even_number_list)

# reduce() function
# syntax of reduce(some_function,iterables[, initial])
# reduce
import functools # explain this part in later in this chapter
number_list=[1,34,78,56,91,44,23]
sum_of_number= functools.reduce(lambda num1,num2:num1+num2, number_list)
print("Output:")
print("Sum of the list are: ",sum_of_number)

# reduce
import functools # explain this part in later in this chapter
number_list=[1,34,78,56,91,44,23]
sum_of_number= functools.reduce(lambda total, num: total + num**2, number_list, 0)
print("Output:")
print("Sum of the list are: ",sum_of_number)

# Another way of using map function.
L1=[2,4,6,8]
L2=[1,2,3,4]
# I want result of addition of each corresponding elements of two lists.
# I also want [3,6,9,12]
s=list(map(lambda a,b:a+b, L1,L2))
print(s)

# Let's try to convert temperature between celcius and farenheit.
# celcius =[37,30,15,100]
# formula= Farenheit= (celcius*9)/5+32
# farheinheit=[]
celcius=[37,30,15,100]
farenheit=list(map(lambda c: (c * 9) / 5 + 32, celcius))
print(farenheit)
