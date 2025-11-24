"""#user input in python 
print("Enter your name:")
name = input()
print(type(name))
#note: python input() function always return string
#in Python, input() always returns a string by default, no matter what the user types.
"""

"""#input integer number in python 
age = int(input("enter your age: "))
print(type(age))
print(age+1)"""

#input float and integr booth 

"""age = float(input("enter your number: "))
print(type(age))"""


try:
    num = float(input("Enter your number: "))
    if num.is_integer():
        print(f"you enteredwew12: ")
    else: 
        print(f"you entered: {num}")

except ValueError:
    print("invalid input")
