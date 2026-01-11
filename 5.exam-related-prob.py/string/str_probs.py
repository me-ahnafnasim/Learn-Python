"""
--basic
#Convert String to List & Back
"""
s = "bangla"
myList = list(s)
con_string ="".join(myList)
print(con_string)

#Note: split-seperate each word from sentence and make a list, not letter from word
str1 = s.split() 




#1)
"""Write a Python program to count the frequency of each character in a 
string using a dictionary."""

myString = 'google.com'
result ={}
for item in myString:
    if item in result:
        result[item] += 1
    else:
        result[item] = 1
print(result)

#or,
myString = 'google.com'
result ={}
for char in myString:
    result[char] = result.get(char, 0)+1
print(result)

# Learn how get() function work under the hood
'''
get(key, default)

-get function take two argument, key, and default
-in our case if key not found by default it add 0 as value
-and after adding extra 1, it make a place in the result
as (a:1)
-if key in the list, it takes the value and add 1
that's why 1 increase from total count
'''
#dict.get(key, default)
d = {'a': 5}
print(d.get('a', 0)+1)   # a:1
print(d.get('b', 0))     # a:0




#2)Get a string's first and last 2 chars..
def cut_str(str):
   if len(str)<2:
    return ""
   else:
    return str[0:2]+str[-2:]

print(cut_str('ahnafnasim'))





#3)
"""
Write a Python program to get a string from a given string where
 all occurrences of its first char have been changed to '$',
 except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
str = "restart"
char = list(str)
first_word = char[0]
for i in range(1, len(char)):
    if char[i] == char[0]:
        char[i] = "$"
new_str = "".join(char)
print(new_str)



#4)

"""
Write a Python program to add 'ing' at the end of a string
 if its length is at least 3, or 'ly' if it already ends 
 with 'ing'.
"""
user_input = input("enter your text: ")
if len(user_input) <2:
    print(user_input)
    if user_input[-3:] == "ing": #user_input.endswith("ing"):
        new_str = user_input + "ly" 
        print(new_str)
    else:
        user_input += "ing"
        print(user_input)


#5)write a program that count longest and return len word in a sentence
def longest_word_length(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return len(longest_word)

# Example usage
sentence = input("Enter a sentence: ")
print("Length of the longest word:", longest_word_length(sentence))




#6) Write a Python program to build a new string containing only
#  characters from even index positions using a loop.

mystr = "Bangladesh"
new_str = list(mystr)
new_list = []
for index, value in enumerate(new_str):
    if index % 2 == 0:
        new_list.append(value)
result = "".join(new_list)
print(result)

#or:

def odd_value_string(mystr):
    result = ""
    for i in range(len(str)):
        if i % 2 != 0:
            result = result + mystr[i]
    return result



#7) Swap first and last chars of a string.

myStr ="abcd"
newStr = list(myStr)
newStr[0], newStr[-1] = newStr[-1], newStr[0]
print("".join(newStr))

#or:

def change_string(str1):
    return str1[-1]+str1[1:-1]+str1[0]
print(change_string('abcd'))


result ="bangladesh"
print(result[0]+result[1])



#8)Write a Python program to count the frequency of each word in a 
# sentence and return a dictionary of word counts.
myStr = "the quick brown fox jumps over the lazy dog."
newStr = myStr.split()
result ={}
for item in newStr:
    if item in result:
        result[item] +=1
    else:
        result[item] = 1
print(result)
#or
myStr = "the quick brown fox jumps over the lazy dog."
s = myStr.split()
result ={}
for word in s:
    result[word] = result.get(word, 0)+1
print(result)




#9) return the len of smallest and longest word from a sentence


myStr = "the quick browns fox jumps over the lazy dog."
newStr = myStr.split()
max_len = None
min_len = None
for word in newStr:
    if max_len is None or len(word) > max_len:
        max_len = len(word)

    if min_len is None or len(word) < min_len:
        min_len = len(word)
print(max_len, min_len)

#or,

myStr ="A quick red fox"
newStr =myStr.split()
result =[]
for item in newStr:
    result.append(len(item))
max_len =max(result)
min_len =min(result)
print(max_len, min_len)

#or 
myStr ="A quick red fox"
ss = myStr.split()
sw =min(ss, key =len)
lw =max(ss, key =len)
print(len(sw), len(lw))


#10)#Write a Python program to find the smallest and largest words in a given string.

myStr = "i am from bangladesh"
words = myStr.split()
#max(words) --Compares strings alphabetically
#max(words, key=len) --Compares strings by their length (what we want)
longest_word = max(words, key = len)
shortest_word = min(words, key = len)
print(longest_word, shortest_word)

#or,

myStr = "i am from bangladesh"
words = myStr.split()
longest = words[0]
shortest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word

print("Longest word:", longest)
print("Shortest word:", shortest)





#11)Find the common values that appear in two given strings(duplicate word allow)
str1 ="bangla"
str2 ="dhakabangladesh"
result =[]
#if char in str2 → checks if the current character is inside str2.
#and char not in result → ensures you don’t add duplicates.
for word in str2:
    if word  in str1:
    #if word not in result and word in str1:
        result.append(word)
print("".join(result))

#or, (duplicate words are not allow)
str1 = 'Pythonn3'
str2 = 'Pythonn2.7'
result =""
for ch in str1:
    if ch in str2 and ch not in result:
        result += ch
print(result)




#12) remove duplicate words in string.
s ="bangladeshhgl"
result =""
for char in s:
    if char not in result:
        result +=char
print(result)

#or
s ="programming"
#dict.fromkeys(s)) -- make a dictionary keys are the char and value is none
#join() only takes the key and remove the tuplicate word and join them togather
result ="".join(dict.fromkeys(s))
print(result)

#or
#string theke dictionary make korele duplicate gula remove hoye jai
# then join(), only key gula add kore return kore
def remDuplicate(str3):
    result ={}
    for char in str3:
        result[char] = 0
    return "".join(result)
print(remDuplicate("naassmm"))




#13) Write a Python program to extract numbers from a given string.
myStr ="red 12 black 45 green"
new_str = myStr.split()
result =[]
for char in new_str:
    if char.isnumeric():
        result.append(char)
print(result)


#14)Write a Python program to check whether any word in a given string 
# contains duplicate characters or not. Return True or False.
def findDuplicate(word):
    word_list = word.split()
    for word in word_list:
        if len(word) > len(set(word)):
            return False
        # If no word with duplicate characters is found, return True
        return True
print(findDuplicate("The wait is over."))
    
#or,

word = "bangladesh"
if len(word) != len(set(word)):
    print("There are duplicate characters")
else:
    print("All characters are unique")






#15)Remove punctuation from string.

def remove_punctuations(text):
    punc_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #onel somoy "\" ekta dile error ase but double dile kono error ase na
    #or   punct =r'''!()-[]{},;:\\./?`@#$%^&*/|_''' samne ekta r diye dilei hoy
    result = ""
    for char in text:
        if char not in punc_list:
            result = result + char
    return result

text1 = "@^&$String! With.-- Punctuation?"
text ="A%^!B#*CD"
result = remove_punctuations(text)
print(result) 



#16) Write a Python program to convert a given string into a list of words.
myStr ="i am from Dhaka, Bangladesh"
new_str = myStr.split()
print(new_str)




#17)Write a Python program to count and display vowels in text.
def countDisplay(myStr):
    newStr = myStr.replace(" ", "").lower()
    vowels = "aeiou"
    vowels_in_str =""
    for char in newStr:
        if char in vowels:
            vowels_in_str += char
    return(len(vowels_in_str), vowels_in_str)

print(countDisplay("Welcome to w3resource.com"))



#18)Write a Python program to find the maximum number of characters in a given string.
def max_char_in_string(str1):
    result ={}
    max_char =0
    word =None
    for char in str1:
        result[char] = result.get(char, 0)+1
    for char in str1:
        if result[char]>max_char:
            max_char = result[char]
            word = char
    return word,max_char
        
print(max_char_in_string("nasimsnaaa"))

#or,

def max_char_in_string(myStr):
    max_count = 0
    most_frequent_char = None

    for char in myStr:
        current_count = myStr.count(char)
        if current_count > max_count:
            max_count = current_count
            most_frequent_char = char
    return (most_frequent_char, max_count )

print(max_char_in_string("amar sonar bangla"))




#19) Write a Python program to reverse a string.
def rev(str1):
    return ''.join(reversed(str1))
print(rev("Python Exercises"))

#or

def rev(str1):
    revStr =str1[::-1]
    return revStr
print(rev("nasim"))




#20) Write a Python program to reverse words in a string.
myStr ="the quick brown fox"
newStr = myStr.split()
revStr = newStr[::-1]
print(" ".join(revStr))





#21) Write a Python program to determine if a string is a
#  pangram (containing every letter of the English alphabet.)

def pangram(str1):
    inputStr = str1.replace(" ", "").lower()
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    
    for char in alphabet:  # Check each letter in the alphabet
        if char not in inputStr:
            return False
    return True
print(pangram("The quick brown Fox jumps over the lazy dog")) 


"""
must_have = {'toothbrush', 'passport', 'phone', 'charger'}
packed = {'toothbrush', 'phone', 'charger', 'laptop', 'passport'}
must_have.issubset(packed)  # True
"""
def pangram(str1):
    inputStr =str1.replace(" ","").lower()
    alphabets =set("qwertyuiopasdfghjklzxcvbnm")
    print(set(inputStr))
    return alphabets.issubset(set(inputStr))
print(pangram("The quick brown Fox jumps over the lazy do")) 



#22)Check Anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    cleaned1 = str1.replace(" ", "").lower()
    cleaned2 = str2.replace(" ", "").lower()
    # Sort the letters and compare
    return sorted(cleaned1) == sorted(cleaned2)

print(sorted("nasim"))
# Test
print(are_anagrams("listen", "silent"))        # True
print(are_anagrams("evil", "vile"))            # True
print(are_anagrams("The Eyes", "They See"))    # True
print(are_anagrams("hello", "world"))          # False

#or
c =['a', 'i', 'm', 'n', 's']
c2 =['a', 'i', 'm', 'n']
print(list(c) == list(c2))


#23) Check for Palindrome
def palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    return False
print(palindrome("Racecar"))


#24)Count Vowels and Consonants
s ="python"
vowels ="aeiou"
vowels_count = 0
const_count =0
for char in s:
    if char in vowels:
        vowels_count +=1
    else:
        const_count +=1
print(vowels_count, const_count)


#25)Capitalize First Letter of Each Word
s = "hello world"
print(s.title())  



#26)dict of char frequencies
s="programming"
result ={}
for char in s:
    if char  in result:
        result[char] +=1
    else:
         result[char] = 1
print(result)



#27) find first non repeating character; if not fount return None
def find_first_non_repeating_char(str1):
    result ={}
    for char in str1:
        result[char] = result.get(char, 0)+1
    for char in str1:
        if result[char] ==1:
            return char
    return None

print(find_first_non_repeating_char("aabbcc"))



#28) find first repeating character; if not fount return None

def find_first_repeating_char(str1):
    result ={}
    for char in str1:
        result[char] = result.get(char, 0)+1
    for char in str1:
        if result[char] > 1:
            return char
    return None

print(find_first_repeating_char("abbcc"))



#29) capitalize the first and the last character of a string or ord
def capitalize_first_last(text):
    words = text.split()
    result = []
    
    for word in words:
        if len(word) == 1:
            # Single letter
            new_word = word.upper()
        elif len(word) == 2:
            # Two letters → both become uppercase
            new_word = word.upper()
        else:
            # 3 or more letters
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        
        result.append(new_word)
    
    return " ".join(result)


# Test
print(capitalize_first_last("hello"))      # "HellO WorlD"
print(capitalize_first_last("python is awesome")) # "PythoN iS AwesomE"









