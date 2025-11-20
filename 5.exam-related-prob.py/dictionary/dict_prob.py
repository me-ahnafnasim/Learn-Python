#sorted syntax
#sorted(iterable, key = None, reverse = False)

d = {"c":2, "a":3, "d":4, "b":2}
#sort a dictionary according to the key(asending to decending order)
sortLst = dict(sorted(d.items()))
print(sortLst)



#1)Sort (ascending(Smallest to Largest)  a dictionary by value


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = dict(sorted(d.items(), key = lambda item : item[1], reverse = False))
print(sorted_dict)

#2) Sort  descending a dictionary by value
sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_d)


#3) Add Key to Dictionary
my_dict = {0: 10, 1: 20}
my_dict[2] = 3
print(my_dict)


#Concatenate following dictionaries to create a new one
#way 1
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1 |= {3:30, 4:40}
dic1 |= {5:50,6:60}
print(dic1)


#way 2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create an empty dictionary 'dic4' that will store the combined key-value pairs from 'dic1', 'dic2', and 'dic3'.
dic4 = {}
# Iterate through each dictionary ('dic1', 'dic2', and 'dic3') using a loop.
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4) 


#way 3
# Merge using dictionary unpacking (**)
merged_dict = {**dic1, **dic2, **dic3}
print( merged_dict)





#)4. Write a Python script to check whether a given key already exists in a dictionary.
def finKey(d, outKey):
    for key in d:
        if key == outKey:
            print("key exist")
            return  # Optional: exit early once found
    print("Key does not exist")  # Optional: let user know if not found

# Dictionary with integer keys
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Convert input to int
outKey = int(input("Enter your key: "))

# Call function
finKey(d, outKey)




#5)Iterate Over Dictionary Using For Loops
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for dict_key, dict_value in d.items():
    print(dict_key, "->", dict_value)



#6)Write a Python program to transform a dictionary into a list of tuples.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dTOt = list(d.items())
print(dTOt)




#7)Create a flat list of all the keys in a flat dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
flatKey = []
for key in d:
    flatKey.append(key)
print(flatKey)

#or,

def test(flat_dict):
    return list(flat_dict.keys())
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(test(d))






# 8) find key of a maximum value in a Dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

max_value = None
max_key = None
for  key, value in d.items():
    if max_value is None or value > max_value:
        max_value = value
        max_key = key
print(max_key)



# find key of a minimum value in a Dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

max_value = None
max_key = None
for  key, value in d.items():
    if max_value is None or value <max_value:
        max_value = value
        max_key = key
print(max_key)
    


result = max(d.items(), key = lambda item:item[1])
print(result)
#unpack the result
max_key, max_value = result
#remember max return the tuple that value is maximum
print(max_key)
print(max_value)






#9) Write a Python program to get the maximum and minimum values of a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
max_value = None
min_value = None
for value in d.values():
    if max_value is None or value > max_value:
        max_value = value
    if min_value is None or value < min_value:
        min_value = value
        
print(max_value, min_value)

#get the max value only
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
max_value = None
for value in d.values():
    if max_value is None or value> max_value:
        max_value = value
print(max_value)


#get the min value only
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
min_value = None
for value in d.values():
    if min_value is None or value<min_value:
        min_value = value
print(min_value)


result = max(d.items(), key = lambda item:item[1])
key, value = result
print(value)






# 10) Replace each list with the sum of its elements
my_dict = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9],
    'd': [10, 11, 12]
}

#type 1:
for index, (key, value) in enumerate(my_dict.items()):
#note: my_dict[key]  indicate a list based on keys(a,b,c,d) and we replace the list by the value
    my_dict[key] = sum(my_dict[key])
print(my_dict)

#type: 2
for key in my_dict:
    my_dict[key] = sum(my_dict[key])
print(my_dict)





#11) Filter each list in the dictionary to keep only the odd integers
my_dict = {
    'a': [1, 2, 3, 7],
    'b': [4, 5, 6, 9],
    'c': [7, 8, 9, 11],
    'd': [10, 11, 12, 23]
}
for key,value in my_dict.items():
    new_list = []
    for item in value:
        if item % 2 != 0:
            new_list.append(item)
    my_dict[key] = new_list
print(my_dict)

#or,
for key, value in my_dict.items():
    result[key] = [x for x in value if x%2 !=0 ] 
print(result)



#12) return a new dictionary by replacing the list by odd and odd max number
my_dict = {
    'a': [1, 2, 3, 7],
    'b': [4, 5, 6, 9],
    'c': [7, 8, 9, 11],
    'd': [10, 11, 12, 23]
}
for key, value in my_dict.items():
    max_odd = None
    for item in value:
         if item%2 != 0:
            if max_odd is None or item > max_odd:
                max_odd = item
    my_dict[key] = max_odd
print(my_dict)

#or,
result ={}
for key, value in my_dict.items():
    result[key] = max([x for x in value if x %2 != 0])
print(result)





"""13) Write a Python function that takes a dictionary where each key maps 
to a list of integers, and returns a new dictionary where each key maps 
to the maximum odd number from its corresponding list. If no odd number 
exists in the list, store None for that key"""
my_dict = {
    'a': [1, 2, 3, 7],
    'b': [4, 5, 6, 9],
    'c': [7, 8, 9, 11],
    'd': [10, 14, 12, 20]
}

def get_max_odd_from_lists(d):
    result = {}
    for key, lst in d.items():
        # Filter odd numbers in the list
        odd_numbers = [x for x in lst if x % 2 == 1]
        # If there are odd numbers, get the max; else set to None or skip
        if odd_numbers:
            result[key] = max(odd_numbers)
        else:
            result[key] = None  # or you can skip or use 0
    return result

# Call the function
max_odds = get_max_odd_from_lists(my_dict)
print(max_odds)




#14) 
"""
Write a Python function max_num(my_dict) that iterates through
a dictionary of lists and constructs a new dictionary
where each value is a list containing the maximum value from the
 corresponding list in the input. Finally, print the new dictionary. 
"""
def max_num_lst(my_dict):
    result = {}
    for key, lst in my_dict.items():
        result[key] = [max(lst)]
    print(result)

print(max_num_lst(my_dict))





#15)
"""
Write a Python function that takes a dictionary with lists as values 
and returns a new dictionary where each key is associated with the 
maximum number from its list.
"""
def max_num_lst(my_dict):
    result = {}
    for key, lst in my_dict.items():
        result[key] = max(lst)
    print(result)
    
my_dict = {
    'a': [1, 2, 3, 7],
    'b': [4, 5, 6, 9],
    'c': [7, 8, 9, 11],
    'd': [10, 14, 12, 20]
}
max_num_lst(my_dict)
print(max_num_lst(my_dict))





#16)What is the sum of all the numbers in the lists of the dictionary below?
my_dict = {
    'a': [1, 2, 3, 7],
    'b': [4, 5, 6, 9],
    'c': [7, 8, 9, 11],
    'd': [10, 11, 12, 23]
}
total =0
for value in my_dict.values():
    for item in value:
        total += item
print(total)



#17) Replace each list with the average of its value(list)
my_dict = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9],
    'd': [10, 11, 12]
}
for key, value in my_dict.items():
    avg = sum(value)/len(value)
    my_dict[key] = avg
print(my_dict)

#type-1
for index, (key, value) in enumerate(my_dict.items()):
    my_dict[key] = round(sum(my_dict[key])/len(value))
print(my_dict)

#type_2
for key,value in my_dict.items():
    my_dict[key] = round(sum(my_dict[key])/len(value), 2)
print(my_dict)





#18)#Write a Python program to iterate through a dictionary and display each key, its value, and an enumeration index starting from 1.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for index, (key, value) in enumerate(dict_num.items(), 1):
    print(key, value, index)



#19)Write a Python program to sum the number of items across all list values in a 
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

#type-1:
total = 0
new_ele = []
for value in dict.values():
    for item in value:
        new_ele.append(item)
print(len(new_ele))

#type-2:
ctr = sum(map(len, dict.values()))
print(ctr) 




#20) Write a Python program to filter a dictionary of student names and 
# (height, weight) tuples and return only those meeting specified thresholds.
students = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (6.1, 68),
    'Pierre Cox': (5.8, 66)
}
result ={}
for key, value in students.items():
    height, weight = value
    if height > 6 and weight>= 64:
        result[key] = (height, weight)
print(result)




#21)
"""
Write a Python program to implement a function that returns a frequency 
dictionary for a given string, ignoring case
"""
str1 = 'w3resource'
result ={}
for key in str1:
    if key in result:
        result[key] +=1
    else:
        result[key] = 1
print(result)




#22)
"""
Write a Python program to implement a function that returns the frequency
 distribution of dictionary values.
"""

d ={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
result ={}
for value in d.values():
    if value in result:
        result[value] +=1
    else:
        result[value] =1
print(result)




#23) Combine Two Lists into a Dictionary
d1 =['a', 'b', 'c', 'd', 'e', 'f']
d2 =[1, 2, 3, 4, 5]

merged ={}
min_len = min(len(d1), len(d2))

for i in range(min_len):
    merged[d1[i]] = d2[i]
print(merged)




#24)Write a Python program to remove the None value from a given list.
def remove_none(nums):
    result = [x for x in nums if x is not None]
    return result
nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print(nums)




#25) Write a Python function group_words(words) that takes a list of strings 
# words and returns a dictionary where: The keys are the first letters of the words (lowercase).
# The values are lists of words that start with the corresponding letter.

words = ["apple", "banana", "cherry", "date", "elderberry", "among"]
result = {}
for word in words:
    if word[0] not in result:
        result[word[0]] = [word]      # first word with this letter
    else:
        result[word[0]].append(word)  # add to existing list
print(result)




#26)Group words by anagram.
words = ["eat","tea","tan","ate","nat","bat"]

anagram_dict = {}   
for word in words:
    key = "".join(sorted(word)) #print(sorted("nasim")) --->['a', 'i', 'm', 'n', 's']
    if key not in anagram_dict:
        anagram_dict[key] = []
    
    anagram_dict[key].append(word)

print(anagram_dict)














#combine multiple dictionaries in to one solution

"""
#1)Write a Python program to combine multiple dictionaries into one by appending values for duplicate keys into lists.
"""
def merged_dicts(*dicts):
    merged = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged:  
                if isinstance(merged[key], list):
                    #jodi merged e age theke key thake tobe just append kora
                    merged[key].append(value)
                else:
                    #e khane merged e age theke ekta value thake, oi value are
                    # notun value add kore merged e notun ekta list create kore
                    #see the below example for better understanding
                    merged[key] = [merged[key], value]
            else:
                merged[key] = value

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'd': 6}
dict3 = {'a': 7, 'e': 8, 'd': 2}

result = merged_dicts(dict1, dict2, dict3)
print(result)


"""
dict1 = {'a': 1, 'b': 2, 'c': 3}
merged ={'a': 4, 'b': 5, 'c': 6}
for key, value in dict1.items():
    merged[key] = [merged[key], value]
print(merged)
"""


"""
#2)Write a Python program to combine multiple dictionaries into one by appending values for duplicate keys into lists.
"""
d1 ={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d2 ={'x': 300, 'y': "red", 'z': 600}

#output ={'w': [50], 'x': [100, 300], 'y': ['Green', 'red'], 'z': [400, 600]}

def merged_dict(*dicts):
    merged ={}
    for d in dicts:
        for key, value in d.items():
            if key in merged:
                if isinstance(merged[key], list):
                    merged[key].append(value)
                else: 
                    merged[key] = [merged[key],value]
            else:
                merged[key] = [value]
    return merged
d1 ={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d2 ={'x': 300, 'y': "red", 'z': 600}
print(merged_dict(d1, d2))





"""
#3)merge two dictionary whose value are list, for same key merged the list and different key just append
"""

def merged_dict(*dicts):
    merged ={}
    for d in dicts:
        for key, value in d.items():
            if key in merged:
                if isinstance(merged[key], list):
                    merged[key].extend(value)
                else:
                    merged[key] = [merged[key], value]
            else:
                merged[key] = value
    return merged

d1 = {'a': [1,5], 'b': [9,0,1], 'c':[2,3,4]}
d2 = {'a': [7,8,4], 'b': [2,3], 'd':[4,9]}

print(merged_dict(d1, d2))




"""
#4) Write a Python program to merge two dictionaries by summing the values of common keys with a loop
note: by using this methods you can merge so many dict togather
"""
def merged_dicts(*dicts):
    merged = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged:  
                merged[key] += value
            else:
                merged[key] = value
    return merged

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'd': 6}
dict3 = {'a': 7, 'e': 8, 'd': 2}

result = merged_dicts(dict1, dict2, dict3)
print(result)






