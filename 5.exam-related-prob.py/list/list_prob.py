"""
1) Returns the largest odd number in the list.
    If no odd number is found, returns None.
    """
def find_max_odd(myList):
    max_num = None
    for num in myList:
        if num % 2 != 0:  # Check if odd
            if max_num is None or num > max_num:
                max_num = num
    return max_num

# Example usage:
myList = [0, 9, 2, 4, 5, 6]
result = find_max_odd(myList)
print(result)



#2)Write a Python program to get the largest number from a list.

myList = [0, 9, 2, 4, 5, 6, 10]
maxNum = None
for num in myList:
    if maxNum is None or num>maxNum:
        maxNum = num
print(maxNum)



#3)Write a Python program to sum all the items in a list.
myList = [0, 9, 2, 10, -5]
total =0
for num in myList:
    total +=num
print(total)

#4)Write a Python program to multiply all the items in a list.
myList = [ 9, 2, 10]
total =1
for num in myList:
    total = total * num
print(total)




#5)Write a Python program to get the smallest number from a list.
myList = [1, 9, 2, 4, 5, 6, 10]
minNum = None
for num in myList:
    if minNum is None or num<minNum:
        minNum = num
print(minNum)



#6) Remove Duplicates from List
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
#1) dict.fromkeys() -- make a dict by taking key from list and set the value None
print(list(dict.fromkeys(a)))

#2) fact - dictionary to list convert korle, dict er just key niye list gotito hoy
di = {"name": "nasim", "village":"chandpur", "book": 2} 
print(list(di))  #output - ['name', 'village', 'book']
#or,
result=[]
for num in a:
    if num not in result:
        result.append(num)
print(result)
    

#7)Write a Python function that takes two lists and returns True if they have at least one common member.
def commonEle(li1, li2):
    newSet =set(li1) & set(li2)
    if len(newSet) >=1:
        return True

li1= [1,3,5,6,7,7,1,3]
li2= [2, 5, 1, 5,3,5,7,1,5]
print(commonEle(li1, li2))

#or,
def common_data(li1, li2):
    result =False
    for x in li1:
        for y in li2:
            if x==y:
                result = True
                return result
print(common_data([1, 2, 3, 4, 5,6, 3], [51, 61, 71, 81, 91,31,41,51,61]))
# Call the 'common_data' function with two lists and print the result
print(common_data([1, 23, 4, 5], [6, 7, 8, 9, 90, 40, 1]))           



#8)Write a Python program to print the numbers of a specified list after removing even numbers from it.
myList =[1, 2, 3, 4, 5, 4, 8]
result =[]
for num in myList:
    if num % 2 != 0:
        result.append(num)
print(result)




#9)Write a Python program to check if each number is prime in a given 
# list of numbers. Return True if all numbers are prime otherwise False.

def is_prime(lst):
    for n in lst:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

# Example usage
print(is_prime([10, 11, 12, 13, 14, 15, 17, 18, 19]))   # false
print(is_prime([2, 3, 5, 7, 11]))   # True
print(is_prime([2, 4, 5, 7]))       # False




#10) Seperate the prime number from a list 
def seperate_prime(lst):
    result =[]
    for n in lst:
        if n < 2:
            continue
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(n)

    return result
print(seperate_prime([1,3,5,7,9,0]))


#11)Write a Python program to find the second largest number in a list.
myli =[1,4,6,7,9,3,45,40]
newNum = sorted(myli, reverse=True)
print(newNum[1])

#or,
myli = [9, 3, 45, 40, 1, 4, 6, 7]
#soet asending using bubble sort
for i in range(len(myli)):
    for j in range(i+1, len(myli)):
        if myli[i] > myli[j]:
            myli[i], myli[j] = myli[j], myli[i]
print(myli)



#12)Write a Python program to get unique values from a list.
#dont maintain the orginal dictionary order
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print(set(my_list))

#maintain the orginal dictionary order
result =[]
for num in my_list:
    if num not in result:
        result.append(num)
print(result)


#13)Write a Python program to get the frequency of elements in a list.
li =[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]   
result ={}     
for num in li:
    result[num] = result.get(num, 0)+1
print(result)    

#or,

li =[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
result ={}
for n in li:
    if n not in result:   
        result[n] = 1
    if n in result:
        result[n] +=1
print(result)



#14)Write a Python program to check whether a list contains a sublist.
#5-2+1=4
#Sublist: the elements must appear in the same order and consecutively inside
def is_sublist(big,small):
    b,s=len(big), len(small)
    for i in range(b-s+1): 
        if big[i:i+s] ==small: 
            return True
    return False

a =[2,4,3,5,7]
b =[4,3]
c =[3,7]
print(is_sublist(a,b))
print(is_sublist(a,c))


"""big[0:2]
big[1:3]
big[2:4]
big[3:5]
"""


#15)Count the number of elements in a list within a specified range

def count_by_range_in_list(li, min_len, max_len):
    ctr =0
    for char in li:
        if min_len<= char <=max_len:
            ctr +=1
    return ctr
list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
print(count_by_range_in_list(list1, 40, 100))
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_by_range_in_list(list2, 'a', 'e')) 



#16)Write a Python program to find common items in two lists.
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
print(set(color1) & set(color2))

#or,
result =[]
for item1 in color1:
    for item2 in color2:
        if item1 == item2:
            result.append(item1)
print(result)


#17) Write a Python program to find the list in a list of lists whose sum 
# of elements is the highest.
def max_sublist_sum(li):
    newLi =[]
    for subLi in li:
        subLiSum = sum(subLi)
        newLi.append(subLiSum)
    return max(newLi)

li = [[1, 2, 3], [4, 5, 6], [10, 11, 12, 2], [7, 8, 9]]
print(max_sublist_sum(li))

#or,
lists = [[1, 2, 3], [4, 5], [10, 1], [2, 2, 2, 2]]
max_list = max(lists, key=sum)
print("List with highest sum:", max_list)
print("Sum:", sum(max_list))



x = [10, 20, 30]
y = [40, 50, 60]
print()
x[:0]=y
print(x)


#18)Write a Python program to extend a list without appending.
x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)




#19)#find the average of the nested list
a = [[2,3,4], [2,7,9,3], [2, 8]]
newl=[]
for xlist in a:
    suma = sum(xlist)
    lenth = len(xlist)
    newl.append(suma/lenth)
print(newl)



#20) get the sum of the nested list
a = [[2,3,4], [2,7,9,3], [2, 8]]
newLi =[]
for subli  in a:
    suma =sum(subli)
    newLi.append(suma)
print(newLi)


#21)Write a Python program to remove duplicates from a list of lists.
li = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
result =[]
for subLi in li:
    if subLi not in result:
        result.append(subLi)
print(result)



#22)Given a nested list (a list of lists), write a function that removes 
# duplicate elements from each individual sublist
def remove_duplicates_each(lst):
    result = []
    for sublist in lst:
        unique = list(dict.fromkeys(sublist))
        result.append(unique)
    return result
nested_list = [[1, 2, 2, 3], [4, 4, 5, 6, 5], [7, 8, 7, 8, 9]]
print(remove_duplicates_each(nested_list))




#23) flatten list

#applicable only for nested list flatten
lst =[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flatten =[]
for num in lst:
    if isinstance(num, list):
        flatten.extend(num)
    else:
        flatten.append(num)
print(flatten)


#applicable for both nested and deep nested list flatten
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # recursion
        else:
            result.append(item)
    return result

nested = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(flatten_list(nested))




#24)Write a Python program to count the number of lists in a given list of lists.
lst =[[1, 3], [5, 7], [9, 11], [13, 15, 17, 4]]
count = 0
for item in lst:
    if isinstance(item, list):
        count +=1
print(count)




#
lst =[[1, 3], [5, 7], [9, 11], [13, 15, 17, 4]]
n = max(lst, key=len)
print(len(n))


lst =[[1, 3], [5, 7], [9, 11], [13, 15, 17, 4]]
n = min(lst, key=len)
print(len(n))

maxLen = 0
minLen =len(lst[0])
for item in lst:
    if isinstance(item, list):
        if len(item) > maxLen:
            maxLen = len(item)
        if len(item) < minLen:
            minLen = len(item)
        
print(maxLen, minLen)





#25) remove empty list from list of list
li = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
result =[]
for item in li:
    if isinstance(item, list):
        if len(item)!=0:
            result.append(item)
    else:
        result.append(item)
print(result)



#26)Write a Python program to convert a given list of strings into a list of lists.

li = ['Red', 'Maroon', 'Yellow', 'Olive']
result =[]
for str in li:
    newLi = list(str)
    result.append(newLi)
print(result)



#27) find the index of maximum value in a list
def max_index(li2):
    max_num =None
    max_num_index = None
    for index, num in enumerate(li2):
        if max_num is None or num> max_num:
            max_num = num
            max_num_index = index
    return max_num_index
print(max_index(li2= [2, 5, 1, 5,3,5,7,1,5]))




#28) reverse a list
lst= [1,3,5,6,7]
reversed_list =lst[::-1]
print(reversed_list)



#29) check if all elements in a list are unique
def unique_element(lst):
    if len(lst) == len(set(lst)):
        return True
    else:
        return False
lst= [2, 5, 1, 5,3,5,7,1]
print(unique_element(lst))



#30) Removing all occurrences of an item from a list
lst= [2, 5, 1, 5,3,5,7,1,5]
item =2
result =[]
for num in lst:
    if num != item:
        result.append(num)
print(result)

#or,
new_list = [x for x in lst if x != item]
print(new_list)




median of a list, but only under the assumption that the list is already sorted.
lst = [1, 3, 7, 4, 6, 8]

if len(lst) % 2 != 0:
    print(lst[len(lst)//2])
if len(lst) % 2 == 0:
    avg = lst[len(lst)//2] + lst[len(lst)//2 - 1]
    print(avg / 2)