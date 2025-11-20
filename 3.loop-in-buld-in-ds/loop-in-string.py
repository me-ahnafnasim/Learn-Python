
#1) for loop(Direct iteratio over characters)
text ="hello"
for char in text:
    print(char)
    #i)Loop starting from the second character (index 1) to the end
    for char in str[1:]:
        print(char)
    #ii) loop that skip the first character
    for i in range(1,len(text)):
       print(f"Index {i}: {text[i]}")

#2) For Loop with Index (using range() and len())
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

#3) For Loop with enumerate() (Index + Character)
for index, char in enumerate(text):
    print(f"Index {index}: {char}")

#4) While Loop (Manual Index Control)
i = 0
while i < len(text):
    print(text[i])
    i += 1  # Don't forget to increment!

#5) Reverse Loop (Backward Iteration)
#i)Using for with range() in reverse:
for i in range(len(text) - 1, -1, -1):
    print(text[i])

#ii)Using slicing in a loop:
for char in text[::-1]:
    print(char)
