# survey:
# who played with the excercise?
# Suggestions?


# pycharm - a frientdly IDE from jetbrains
# Great pycharm tutorials
# https://www.youtube.com/watch?v=5rSBPGGLkW0
# Hebrew (starting at 2:10):   https://www.youtube.com/watch?v=tu6xYIIf6H4


# GREAT GREAT GREAT python tutorials from "tech with tim":
# https://www.youtube.com/playlist?list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm

# pycharm gives us great capabilities:
# for example suggestions:
# impo fo
# or debug:
a = 8
b = 4
c = a+b
print(c)
# create d = c+19 in debugger console
c = c+a

# 1. loops
fruits = ["apple", "banana", "cherry", "Pineapple"]
for x in fruits:
    print(x)
for index in range(6):
    print(index)
for index in range(1, 3):
    print(index)
for index in range(1, 3):
    print(fruits[index])




# Self excercise :
# create list with jumps of 2 (using a loop), and print (2,4,6,8,10)

### solution
minRange = 2
maxRange = 11
jumps = 2
list2 = [x for x in range(minRange, maxRange, jumps)]
print(list2)

# ##### 2 string revisited
# txt = "Hello World"[0:8:1]
# print(txt)
# ### multiline string
# txt = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(txt)

## check if a string in a list is only text of numbers
list1 = ["asd12", '123']
print(list1[0].isnumeric())
print(list1[1].isnumeric())

# self excecise: Remove empty strings from a list of strings
# Given:
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
# Original list of sting
# ["Emma", "Jon","", "Kelly", None, "Eric", ""]
# After removing empty strings
# ["Emma", "Jon", "Kelly", "Eric"]

### solution: we use the filter function
##str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
##print("Original list of string")
##print(str_list)
##
### use built-in function filter to filter empty value
##new_str_list = list(filter(None, str_list))
##
##print("After removing empty strings")
##print(new_str_list)


# 3. libraries
##import math
##print(math.pi)

## random library
##import random
##print("Random integer from 100 to 900")
##num1 = random.randint(100, 900)
##print("Random integer: ", num1)


##maxRange = 10
##minRange = 5
##num2 = random.random()*(maxRange-minRange)+minRange
##print(num2)


# self excercise  homework:
# 1. Given an input string save into list where each word is an element in the list. print the list
# 2. Given an input string save into list where ',' is the separator
# 3. Given an input string, count occurrences of all characters within a string
# Given:
# str1 = "Apple"
# Expected Outcome:
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}
# 4. get first name from user. get age from user. if age>18 get last name and print full name

# for more excecise and solutions visit: https://pynative.com/python-string-exercise/


##### solution 1
##txt = "welcome to the jungle"
##x = txt.split()
##print(x)
### solution 2
##txt = "welcome to , the jungle"
##x = txt.split(',')
##print(x)
### solution 3
##str1 = "Apple"
##countDict = dict()
##for char in str1:
##  count = str1.count(char)
##  countDict[char]=count
##print(countDict)
##### solution 4
##getFirstNameStr = "enter your first name :" 
##print(getFirstNameStr)
##firstNameInput = input()
##
##ageInput = input("enter your age :\n")
##age = float(ageInput)
##
##if age > 18:
##    lastNameInput = input("enter your last name :\t")
##    fullName = firstNameInput + " " +lastNameInput
##    ouput = "Hello " + fullName
##    print(ouput)
##else:
##    print("you are under 18 !!!")
