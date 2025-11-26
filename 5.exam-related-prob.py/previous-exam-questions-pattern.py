
#Write a program that takes the last item from a list and inserts it at the start."
lst = [2,5,6,7,9]
last_num = lst.pop()
lst.insert(0, last_num)
print(lst)



'''
Given a dictionary of fruits where each value is a list containing [price, quantity], calculate the total value (price × quantity) 
for each fruit, and determine the maximum total value.
'''

fruits = {
    "apple": [1.20, 50],      
    "banana": [0.50, 100],
    "orange": [0.80, 75],
    "mango": [2.00, 30],
    "grape": [3.50, 20]
}
result =[]
max_price = None
for value in fruits.values():
    total =1
    for item in value:
        total *= item
    result.append(total)
for value in result:
    if max_price is None or value > max_price:
        max_price = value
print(result, max_price)




"""
Write a Python function group_words(words) that takes a list of strings words and returns a dictionary where:
The keys are the first letters of the words (lowercase).
The values are lists of words that start with the corresponding letter.

def group_words(words):
    grouped = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(word)
    return grouped

words = ["apple", "banana", "cherry", "date", "elderberry", "among"]
print(group_words(words))""" 




words = ["apple", "banana", "cherry", "date", "elderberry", "among"]
result = {}
for word in words:
    if word[0] not in result:
        result[word[0]] = [word]      # first word with this letter
    else:
        result[word[0]].append(word)  # add to existing list
print(result)








"""
#Write a function merge_dicts(d1, d2) that merges two dictionaries of lists, appending values for matching keys.

def merged_dict(d1, d2):
    merged = {}
    for key in d1:
        #er mane holo jokon amra merged dictionary ke modify korbo, main dictionary er  na. only upor kono /merged dictionary er values change hobe
        merged[key] = d1[key].copy() #with copy called just shallow copy not the (only the reference is copied, not the object itself).
    
    for key in d2:
        if key in merged:
            merged[key].extend(d2[key]) #key ensure that its not changing the main d1 as well as as during operation
        else:
            merged[key] = d2[key].copy()

    return merged

dict1 = {'a': [1, 2], 'b': [3, 4]}
dict2 = {'a': [5, 6], 'c': [7, 8]}

result = merged_dict(dict1, dict2)
print(result) 
"""




"""
# count uppercase and lowercase words from a string
def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return (upper, lower)

s ="Hello"
called = count_case(s)
print(called)
"""



"""
How do you write a function in Python that returns the common elements of two lists, without duplicates,
 preserving the order from the first list?

def common_elements(a, b):
    result = []
    for item in a:
    #ekhane item hocche a er element, if a er element result e na thake and b 
    # te thake tobe setake result e appeend kora
        if item not in result and item in b:
            result.append(item)
    return result
"""





"""
Write a function that checks if there exists any triplet of consecutive numbers in a list that is either: 
Strictly increasing : like 1 < 2 < 3, or
Strictly decreasing : like 5 > 3 > 1
If such a triplet exists, return True. Otherwise, return False.

conditions:
1) the length of the list cant be <3
2)what will happen if we dont -2 and not do? 

lst =[1, 2, 3, 6, 7, 8]
if len = 6, i=0,1,2,3,4,5

a =5
b =5+1
c =5+2
here, as you can see the index range out of the list

range(len(lst) - 2)
(6-2)=4, if len=4, i=0,1,2,3
a= 3
b= 3+1
c= 4+1
its not out of the range





def has_consecutive_triplet(lst):
    if len(lst) < 3:
        return False
    for i in range(len(lst) - 2):
        a, b, c = lst[i], lst[i + 1], lst[i + 2]
        if (a < b < c) or (a > b > c):
            return True
    return False

"""



"""
#Write a function sum_dict_values(d) that takes a dictionary d as input, where each value is a list of 
numbers. The function should return a new dictionary where each key remains the same, but each list value 
is replaced by the sum of its elements.




def sum_dict_values(d):
    result = {}
    for key in d:
        result[key] = sum (d[key])
    return result

d={
    "a":[2,4,4],
    "b":[3,2],
    "c":[2]
}
call = sum_dict_values(d)
print(call)
    
"""


"""
#Write a Python function called flatten(nested_list) that recursively flattens a nested 
# list and returns a single-level (flat) list containing all the elements in order



print(flatten([1, [2, [3, [4]], 5]]))
# Output: [1, 2, 3, 4, 5]

"""


"""
#write a function count_vowels(s) that takes a string s as input and returns the number of vowels in the string.

def count_vowels(s):
    # s_conv=s.lower()
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0
    for char in s_conv:
        if char in vowels:
            vowel_count += 1
    return vowel_count
"""


"""
#Write a Python function factorial(n) that returns the factorial of a non-negative integer n. 

def factorial(n):
#the factorial of 1 and 0 is 1
    if n == 0 or n == 1
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
"""


"""
#Write a Python function tuples_to_dict(tuples)
#  that takes a list of tuples (each with two elements) and returns a dictionary.
def tuples_to_dict(tuples):
    result = {}
    for key, value in tuples:
        result[key] = value
    return result


tuple_list = [("name", "Alice"), ("age", 25), ("job", "Engineer")]
dictionary = tuple_to_dict(tuple_list)
print(dictionary)
"""



"""
Write a function alternate_case(s) that returns the input string with alternating uppercase and lowercase 
letters, starting with uppercase.


def alternate_case(s):
    result = []
    # i is the index, c is the charectar(value). if a char's(value) index is even it will convert in upper case otherwise it will in lower
    #iterate over a sequence (like a list, tuple, or string) while keeping track of both the index and the value of each element.
    # result=["a","b","c","d","e"]
    #sum ="".join(result)-->hello, sum =" ".join(result)-->h e l l o
    for i, c in enumerate(s):
        if i % 2 == 0:
            result.append(c.upper())
        else:
            result.append(c.lower())
    return ''.join(result)
"""



"""
#find the average of the nested list
a = [[2,3,4], [2,7,9,3], [2, 8]]
newl=[]
for xlist in a:
    suma = sum(xlist)
    lenth = len(xlist)
    newl.append(suma/lenth)
print(newl)


#solve in another way
a = [[2,3,4], [2,7,9,3], [2, 8]]

def ds_ave(xlist):
    average = []
    for sublist in xlist:
        for item in sublist:
            total = total + item
            count = count +1
        avg =total/count
        average.append(avg)
    return average
"""





"""
3rd attempt questuion

1. write a program that take a input from user as string and make it reverse
2. write a program that return the nested list element based max and the odd
example-- ["a":[10, 30, 56], "b":[11, 38, 57], "c":[1,2,5, 34]]
3.
4.
"""









#Write the Python function onlyodd(xlist), xlist being a 
# list of 10 integers in the range (1,20),
#  that returns a list containing only the odd
#  numbers contained in the list xlist.
def onlyodd(xlist):
    return [x for x in xlist if x%2 != 0]
#or
def onlyodd(xlist):
    result =[]
    for num in xlist:
        if num % 2 != 0:
            result.append(num)
    return result
print(onlyodd([1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

    



#Write a function digit_sum(n) that e 
# recursively returns the sum of the digits
#  of an integer n.

def sumdigit(n):
    num = abs(n)
    if num <10:
        return num
    else:
        return (n%10) + sumdigit(n//10)
print(sumdigit(1239))






#Write the Python function a11 unique that returns True
# if all elements in a list are unique, False otherwise.

def unique(xlist):
    if len(set(xlist)) == len(xlist):
        return True
    else:
        return False
print(unique([1,2,3,4,5,6]))





'''
xlist = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]
Implement the Python function ds_oddmax(xlist) 
that returns a list containing the maximum elements contained
 in the inner lists having an odd number of elements.

 -jei inner list gula odd number of element contain korte ce tader max number niye
 ekta list return korte hobe.
'''



def oddmax(xlist):
    result = []
    for inner_list in xlist:
        if len(inner_list) % 2 == 1:  # Check if the number of elements is odd
            result.append(max(inner_list))
    return result
xlist = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]
print(oddmax(xlist))




'''
return a new list which contain odd max number from the sublist
'''
def ds_oddmax(xlist):
    result = []
    for inner_list in xlist:
        odd_numbers = [x for x in inner_list if x % 2 == 1]
        if odd_numbers:  # non-empty → at least one odd number
            result.append(max(odd_numbers))
    return result
#or
def ds_oddmax(xlist):
    result = []
    for inner_list in xlist:
        odd_list= [x for x in inner_list if x % 2 == 1]
        if len(odd_list)>0:  # non-empty → at least one odd number
            result.append(max(odd_list))
    return result
xlist = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]
print(ds_oddmax(xlist))




"""
Write a Python function that calculates the discounted price given
 an original price and a discount percentage, and returns the result 
 rounded to two decimal places. 
"""
def apply_discount(price, dicount_percentage):
    discountPrice = price - (price * dicount_percentage/100 )
    discountPriceRound = round(discountPrice, 2)
    return discountPriceRound

price = 75.50
di_per = 15
print(apply_discount(price, di_per))






"""
"Write a Python program that asks the user for a string and prints it in all uppercase letters." 
This 
"""

userInput = str(input('enter a string: '))
print(userInput.upper())







"""
Write a program that asks the user for a sentence
and prints the sentence in reverse order.
"""
me ='me ahnaf nasim from bangladesh'
split = me.split()[::-1]
result = ' '.join(split)
print(result)


#reverse a word word
me ='ahnaf'
print(me[::-1])






'''
Write a Python function called alternate_case(s) that takes a string 
s and returns a new string where the characters alternate between 
uppercase and lowercase, starting with uppercase at index 0. 
'''
def alternate_case(s):
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:  # Even index (0, 2, 4...) → uppercase
            result.append(char.upper())
        else:           # Odd index (1, 3, 5...) → lowercase
            result.append(char.lower())
    return ''.join(result)





"""
write a Python function called count_tuples(tuples) that takes
 a tuple as input and returns a dictionary where: 

Each unique element in the tuple is a key, and
The corresponding value is the number of times that element appears
 in the tuple.
"""

def count_tuples(tuples):
    count_dict = {}
    for element in tuples:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    return count_dict
result = count_tuples(('a', 'b', 'a', 'c', 'b', 'a'))
print(result)  # Output: {'a': 3, 'b': 2, 'c': 1}





'''
Write a Python function called tuples_to_dict(tuples) that takes a 
list of tuples as input and returns a dictionary.

-The first element of each tuple becomes a key in the dictionary.
-The second element of each tuple becomes the corresponding value.
'''

def tuples_to_dict(tuples):
    result = {}
    for key, value in tuples:
        result[key] = value
    return result

# Example 1
print(tuples_to_dict([('a', 1), ('b', 2)]))
# Output: {'a': 1, 'b': 2}

# Example 2
print(tuples_to_dict([('name', 'Alice'), ('age', 30), ('city', 'NYC')]))
# Output: {'name': 'Alice', 'age': 30, 'city': 'NYC'}






'''
Write a Python function called factorial(n) that takes a non-negative
integer n and returns its factorial
'''

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)



def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result





'''
Write a Python function called count_vowels(s) that returns the 
number of vowels in the string s. 
'''

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count








'''
Write a Python function called count_case(s) that takes a string s 
and returns a tuple (uppercase_count, lowercase_count)
 — the number of uppercase letters and lowercase letters in the string. 
'''

def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)
