# tirgul 7 - Functions
# So far you have used python built in functions, such as print().
# In this tutorial you will learn how to create your own user-defined functions
# can someone draw a circle on the board?


# 1. functions start:
# def printMe(str):
#     "This prints a passed string into this function"
#     print(str)  # put a breakpoint and explain callstack
#     return

# call the function. you all have called function before
# printMe("ME")

# 2. data Arguments are passed by reference
# def myFun(x): # note that documentation is not a must
#     x[0] = 20


# # function call
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# def doubleX(x):
#     ans = x*2
#     return ans


# # function call
# print("doubleX = ", doubleX(8))


# # pass by value: Exercise: Try to guess the output of following code.
# # debug the funciton
# def swap(x, y):
#     temp = x
#     x = y
#     y = temp
#     return x, y


# # Driver code
# num1 = 2
# num2 = 3
# resX, resY = swap(num1, num2)
# print("resX:\t", resX)
# print("resY:\t", resY)

# # self excecise: return the Norma of a,b. i.e. c = sqrt(a^2+b^2)
# # example 5 = sqrt(3^2+4^2)=sqrt(9+16)=sqrt(25)=5


# def calcPitagoras(num1, num2):
#     return math.sqrt(num1**2 + num2**2)


# num1 = 3
# num2 = 4
# print("norm of", num1, "and", num2, "=", calcPitagoras(3, 4,))


# def printMatLines(matrix):
#     for raw in matrix:
#         print(raw)


# # using
# matrix = [["1a", "1b", "1c"], ["2a", "2b", "2c", ], ["3a", "3b", "3c"]]
# printMatLines(matrix)


# def printMat(matrix):
#     for raw in matrix:
#         for col in raw:
#             print(col, end=" ")  # print all lines. end
#         print()


# printMat(matrix)


# # Python program to demonstrate
# # default arguments
# def myFun(x, y=50):
#     return x+y


# # Driver code (We call myFun() with only
# # argument)
# result = myFun(10)
# print("result = ", result)


# # Python program to demonstrate Keyword Arguments
# def student(firstname, lastname):
#     print(firstname, lastname)


# # Keyword arguments
# student(firstname='I Love', lastname='Programming')
# student(lastname='Programming', firstname='I Love')


# self excercise: Write a function that recieves 2 numbers of a range separated by ';' and prints
# a random number between them.

# for example for the input: 10;20 the output will be: 14
# function definition:
# def randNumber(str):
# function call:
# print("The random number is: ", randNumber("10;50"))










# import random

# def randNumber(str):
#     num = str.split(";")
#     fromNum = int(num[0])
#     toNum = int(num[-1])
#     return random.randint(fromNum, toNum-1)


# print("The random number is: ", randNumber("10;50"))

# # now let's use this method for random selection between 2 ranges:
# # assume range 1 and range 2, a random range is selected and then a random number is selected from the selected range.
# # # program b
# twoRangeStr = "10;50 80;800"
# ranges = twoRangeStr.split()
# selectedRange = ranges[random.randint(0, 1)]
# result = randNumber(selectedRange)
# print("The random of 2 numbers is: ", result)


# self learning:
# 1 https://www.youtube.com/watch?v=9Os0o3wzS_I
#   https://www.youtube.com/watch?v=EHzKEh74sJI
#   https://www.youtube.com/watch?v=nrCAxXfRU28&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=29


# return abs value of a number:
# i.e. for print(absolute_value(-4))
# ouput: 4


# 2. solution:
# def absolute_value(num):
#     """This function returns the absolute
#     value of the entered number"""

#     if num >= 0:
#         return num
#     else:
#         return -num


# print(absolute_value(2))
# print(absolute_value(-4))
