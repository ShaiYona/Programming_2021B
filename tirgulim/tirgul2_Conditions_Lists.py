
# 1. Conditions: > < == != (bigger, smaller, is equal, is not equal
##print(18>2)
##print(18<2)
##print(18==2) # do not confuse with '='. this is '=='
##print(18!=2)

#### 2. complex numbers
#### like float, int - there are also comlex numbers
##z = complex(3,5.1)
##print(z)


### 3. round numbers to nearest integer
##print(round(1.3))


### 4 casting and types
# print("1"+"2")
# print(int("1")+int("2"))
### Type of input is always str, + operator results in concatination
### Casting will solve this:
### A variable name is a shortcut to it's memory adress
## num1 ="15"
## num2 = "18"
##print(float(num1)+float(num2))
### or save to variable
##res = float(num1)+float(num2)
##print(res)

# 5 if else
# a = 5
# b = 3
# if a > b:
#     print("a>b")
# else:
#     print (" a <= b")


# self excercise: get input a number from user.
# print "positive" if input>0, else print "not positive"



# solution
# num = input()
# if num > 0:
#     print("positive")
# else:
#     print("not positive")  # why not negative?

# self excercise: get input a number from user.
# print "positive" if input>0, "zero" if 0 and "negative" otherwise



# solution
### 6 if else if 
##num = float(input("insert number:\n"))
##if num > 0:
##     print("positive")
##elif num == 0:
##     print("zero")
##else:
##   print("negative")

#### 7 lists
#### link to tutorial and examples:
#### https://www.tutorialspoint.com/python/python_lists.htm
#### contain items - not necessary of same type.
##list1 = ['physics', 'chemistry', 1997, 2000];
##list2 = [1, 2, 3, 4, 5 ];
##list3 = ["a", "b", "c", "d"]
### access items in list
##print(list1[0]) # index starts from 0
##print(list2[1:3]) # range index, places 1 and 2
### update lists
##list2[0] = 8
##print(list2) # print all items
##print(list2[-1]) # print last item - lists are cyclic
##print("length of list is: ", len(list2))
### delete
##del(list2[3])
##print(list2)

### 8 loops
##fruits = ["apple", "banana", "cherry","Pineapple"]
##for x in fruits:
##  print(x)
##for index in range(6):
##  print(index)
##for index in range(1,3):
##     print(index)
##for index in range(1,3):
##     print(fruits[index])

#### 9 string
##myStr = "aba"
##myStr = "ima" # create a new string
### string are immutable and cannot be override
##myStr[1] = 'g'

