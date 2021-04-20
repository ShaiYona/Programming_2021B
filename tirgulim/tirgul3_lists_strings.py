# Important keywords for Product Manager (Chef Master)
# https://www.facebook.com/MicrosoftRnDil/videos/1090576338109340/



# Rescheduele 22.4.21 (morning or 21.4.21)

# 1. random numbers:
import random # import library random

num = random.random() # produce a real number between 0 to 1
print(num)

# self excercise: generate a real number between 50 to 60
num = 50+10*random.random() # 50 - the lower limit, 10 - the range
print(num)




print(random.randint(3, 9))


# self excercise: create a list of 3 random numbers in range 100 to 500


randList = []
for k in range(3):
    randList.append(random.randint(100,500))

print(randList)




##### 2 string revisited
text = input("Enter your string:\t")
print(text[0:5:1] ) # first 5 characters
print(text[0:10:2] )
# reverse a string
print(text[::-1] ) # start at the end, backward
print(text[::-2] ) # start at the end, backward each 2 elements
# rotate a string:
rotatedText = text[2:] + text[:2] # 2 characters right rotation
print(rotatedText ) 

# self excercise: 3 characters left rotation
text = "example"
rotatedText = text[-3:] + text[:-3] # 3 characters left rotation
print(rotatedText ) 

### 3 Repeat loops
##fruits = ["apple", "banana", "cherry","Pineapple"]
##for x in fruits:
##  print(x)
##for index in range(6):
##  print(index)
##for index in range(1,3):
##     print(index)
##for index in range(1,3):
##     print(fruits[index])




#### 4 lists
#### link to tutorial and examples:
#### https://www.tutorialspoint.com/python/python_lists.htm
#### contain items - not necessary of same type.
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [15, 1, 2, 3, 4, 5 ]
# list3 = ["a", "b", "c", "d"]

# # list3.append("e") # add item at end of list
# # print(list3)
# # list1.extend(list2) # add several elements at the end
# # print(list1)
# # list2.append(list3) # what would be the result?
# # print(list2)


# # # sort list
# list4 = [5,2,6,2,2,1]

# ### self excersize - sort the list, use the net




# list4.sort()
# print(list4)
# # insert into list
# list4.insert(2,19)
# print("inserted 19", list4)
# # remove
# list4.remove(19)
# print("removed 19",list4)

# ### Self excersize:
# # 1. from list1, create the list ['physics',2000]
# # 2. print the type of the first element in list1

# ### answer
# list1 = [list1[0],list1[3]]
# print(list1)
# print(type(list1[0]))
# ### self excersize: save list elements that are bigger than 2

# ###ans
# print(list2)
# matches = [x for x in list2 if x > 2]
# print(matches)
# print(type(matches))

# # empty list
# list1 = []
# # create the list: [2, 4, 6, 8, 10]


# for num in range(1,11):
#    if (num%2==0):
#        list1.append(num)
# print(list1)




### multiline string
# text = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(text)




# self learning:
# * Read and run the class again.
# * Read from: https://www.tutorialspoint.com/python/python_lists.htm
# Excercises with Solutions:
##1. Reverse a given list in Python
# Given: aLsit = [100, 200, 300, 400, 500]
# Expected output: [500, 400, 300, 200, 100]

# 2. Given a Python list of numbers. Turn every item of a list into its square
# Given:
# aList = [1, 2, 3, 4, 5, 6, 7]
# Expected ouput:
# [1, 4, 9, 16, 25, 36, 49]







# Solution:
##1.
##aList = [100, 200, 300, 400, 500]
##aList = aList[::-1]
##print(aList)


# 2.
##aList = [1, 2, 3, 4, 5, 6, 7]
##aList =  [x * x for x in aList]
##print(aList)

