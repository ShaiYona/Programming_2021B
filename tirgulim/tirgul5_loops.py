# survey - how many read the file

# tirgul 5

# while loops
# 1. increment
# i = 1
# while i < 6:
#    print(i)
#    i += 1

## 2. break
##i = 1
##while i < 6:
##    print(i)
##    if i == 3: # break condition
##        break
##    i += 1

## 3. continue - skip an iteration
# i = 0
# while i < 6:
#    i += 1
#    if i == 3:
#        continue
#    print (i)

### 4. self excercise: print (10,8,4,2) using while loop
#### decrement
##i = 12
##while i > 2:
##    i -= 2
##    if i==6:
##        continue
##    print(i)
##
### 5. self excercise: save 10,8,4,2 into list. print the list
##i = 12
##myList = []
##while i > 2:
##    i -= 2
##    if i==6:
##        continue
##    myList.append(i)
##
##print(myList)

# 6. loop forever bug
##i = 10
##while i > 6:
##    print(i)
##    i += 1 # defect here. ctrl+c to break run

### 7. while true
##passcode = "Secret"
##isPassed = False
##while not isPassed:
##    inputStr = input ("enter passcode:\t")
##    if inputStr == passcode:
##      isPassed = True
##    else:
##        print("Wrong username or password")
##
##print("permission granted")


# 8. self excercise: factorial with while loop
# calculate all factorials until 9 and store in list.
# print the populated list
##n = 9
##factList = []
##fact = 1
##i = 1
##while i <= n:
##    fact = fact * i
##    factList.append(fact)
##    i = i + 1
##
##print(factList)

### 9. zip function (named after physical zip, just like in jeans)
##s1 = {2, 3, 1}
##s2 = {'b', 'a', 'c'}
##zipRes = zip(s1, s2)
##result = list(zip(s1, s2))
##print(result)
##print(type(zipRes))
##print(zipRes)
# 3 way zipping
##s1 = {2, 3, 1}
##s2 = {'b', 'a', 'c'}
##s3 = {'s31','s32','s33'}
##result = list(zip(s1, s2,s3))
##print(result)

### 10. dictionary:
##keys = ['Ten', 'Twenty', 'Thirty']
##values = [10, 20, 30]
##sampleDict = dict(zip(keys, values))
##print(sampleDict)
##
### 11. self excecise dictionary:
### merge 2 dictionaries into one.
##dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
##dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
##
##
### solution:
##dict3 = dict1.copy()
##dict3.update(dict2)
##print(dict3)
##
### another way
##dict3 = {**dict1, **dict2}


### Self learning homework:
# 1. learn about tuple - immutable list. https://www.programiz.com/python-programming/tuple
# 2. learn about zip: a. https://realpython.com/python-zip-function/
#                     b. https://www.youtube.com/watch?v=HelKJsDIH8k
# 3. learn about dictionary: a. https://www.youtube.com/watch?v=daefaLgNkw0
#                            b. https://www.w3schools.com/python/python_dictionaries.asp





