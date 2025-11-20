#1)For Loop with Index (using range): Loop through list by index.
#note: for i in range(start, end, steps)
# koto theke start hobe like(0,1,2)
#max koto porjonto cholbe 
#koto gor porjonto kore increase hobe
for i in range(1, 10, 1):
    print(i)


#2) start and step na thakle
# zero theke start hoy
#finally 9 porjonto jai
for i in range(10):
    print(i)



#3) For Loop: The most common way to loop through list items directly.
my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)



#4)For Loop with Index (using range and len): Loop through list by index
for i in range(len(my_list)):
    print(my_list[i])



#5)For Loop with enumerate(): Gets both the index and value in the loop.
#note: enumerate(iterable, start=0)
for i, item in enumerate(my_list):
    print(i, item)



#6)Using a for Loop with Slicing or Steps
my_list = [0, 1, 2, 3, 4, 5]
for item in my_list[::2]:  # Every second item
    print(item)




#7)
"""
The map() function in Python is used to apply a given function to each
 item in an iterable (like a list, tuple, etc.) and returns a map 
 object (which is an iterator). You can convert the result to a list,
tuple, or set if needed.

syntax:
map(function, iterable, ...)

-function: A function that will be applied to each element of the iterable.
-iterable: One or more iterables (lists, tuples, etc.).
-If multiple iterables are passed, the function must accept that many arguments.
"""
#example: Single iterable
# Define a function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))  # Output: [1, 4, 9, 16, 25]



#using lambda
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 2, numbers)
print(list(result))  # Output: [1, 4, 9, 16, 25]


#multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# Add corresponding elements
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # Output: [5, 7, 9]





def square(x):
    return x**x
numbers =[1,4,5,6]
result = map(square, numbers)
print(list(result))