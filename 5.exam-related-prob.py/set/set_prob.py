#1)Write a Python program to create a set.
x =set()
print(type(x))

#error dibe 
n = set(0, 1, 2, 3, 4)
print(n)

#2) Create a non-empty set 'n' with the elements 0, 1, 2, 3, and 4 using a set literal:
n = set([0, 1, 2, 3, 4])
print(n)


#3)Find Maximum and Minimum Values in a Set
setn = {5, 10, 3, 15, 2, 20}
print(max(setn))
print(min(setn))



#4)Write a Python program to find the length of a set.
setn = {5, 5, 5, 5, 5, 5}
print(len(setn))



#5)Write a Python program to check if two given sets have no elements in common.
# isdisjoint()--check weather two set have common element or not
#if no common element then return --TRUE
x = {1, 2, 3}
y = { 5, 6, 7}
z = {8}
print(x.isdisjoint(y))
