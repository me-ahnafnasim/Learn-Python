<div align="center">
<h1>Python list </h1>
</div>

<h2 1.  style="color:red">list Constructor </h2>

```python
Assignment in Python: Direction Matters
In Python, the left side of the assignment operator (=) is the name (variable) that will refer to the object on the right side .

a = 10
b = a
b = 20

print(a)  # Still 10
print(b)  # Now 20

a = b     # Now a becomes 20
print(a)  # 20

a = 10 Make a refer to the value 10
b = a Make b refer to whatever a refers to
a = b Make a refer to whatever b refers to
```

```python
empty_list = list()
print(empty_list)  # Output: []

#2. From a String
chars = list("hello")
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']

# from a tuple
tup = (1, 2, 3)
lst = list(tup)
print(lst)  # Output: [1, 2, 3]

#from a set
s = {3, 1, 2}
lst = list(s)
print(lst)  # Output: [1, 2, 3] (order may vary since sets are unordered)


d = {'a': 1, 'b': 2}
lst = list(d)
print(lst)  # Output: ['a', 'b'] (only keys are added to the list)
#Note:
print(list(d.values()))   # Output: [1, 2]
print(list(d.items()))    # Output: [('a', 1), ('b', 2)]


x = 1234
listx = list(x)
#output: TypeError: 'int' object is not iterable

```

<h2>
What Does It Mean That a List Is Mutable in Python?
</h2>
In Python, "mutable" means that the contents of an object can be changed after it's created.

Since lists are mutable , you can:

Add, remove, or change elements
Modify elements in place
Sort, reverse, or otherwise alter the list without creating a new object

```python
example:
# Original list
numbers = [1, 2, 3]
print("Original:", numbers)  # [1, 2, 3]

# Change an element
numbers[0] = 10
print("After change:", numbers)  # [10, 2, 3]

# Add an element
numbers.append(4)
print("After append:", numbers)  # [10, 2, 3, 4]

# Remove an element
numbers.remove(2)
print("After remove:", numbers)  # [10, 3, 4]
```

<h2> List Methods</h2>

## 🎯 Python List Methods: A Complete Reference

---

### 1. `append()` ➕

**Adds an element at the end of the list**

```python
fruits = ['apple', 'banana']
fruits.append('cherry')
# Result: ['apple', 'banana', 'cherry']
```

---

### 2. `insert()` 📥

**Inserts an element at a specific position**

```python
fruits = ['apple', 'banana']
fruits.insert(1, 'blueberry')
# Result: ['apple', 'blueberry', 'banana']
NOTE: If the index greater than list length, it add the element at the end of the list
```

---

### 3. `extend()` 📚

**Adds all elements of an iterable to the end**

```python
fruits = ['apple', 'banana']
fruits.extend(['cherry', 'date'])
# Result: ['apple', 'banana', 'cherry', 'date']
```

---

### 4. `pop()` 🧼

**Removes and returns an element (default last)**

```python
fruits = ['apple', 'banana', 'cherry']
item = fruits.pop()
# item: 'cherry', fruits: ['apple', 'banana']
Note:
1)index (optional): The position of the element to remove and return.

2)If no index is specified, it removes and returns the last element .
3)index out of range error arise, modify the orginal list
```

---

### 5. `remove()` 🗑️

**Removes the first occurrence of a value**

```python
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
# Result: ['apple', 'cherry']
```

---

### 6. `clear()` 🧹

**Removes all elements from the list**

```python
fruits = ['apple', 'banana']
fruits.clear()
# Result: []
```

---

### 7. `copy()` 💾

**Returns a shallow copy of the list**

```python
fruits = ['apple', 'banana']
new_list = fruits.copy()
# new_list: ['apple', 'banana']
```

---

### 8. `count()` 🔢

**Counts how many times an element appears**

```python
nums = [1, 2, 3, 2]
nums.count(2)
# Result: 2
```

---

### 9. `index()` 🔍

**Returns index of the first occurrence**

```python
fruits = ['apple', 'banana', 'cherry']
fruits.index('cherry')
# Result: 2
```

---

### 10. `reverse()` 🔁

**Reverses the list in place**

```python
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
# Result: ['cherry', 'banana', 'apple']
```

---

### 11. `sort()` 🧮

**Sorts the list in ascending order**

```python
fruits = ['banana', 'apple', 'cherry']
fruits.sort()
# Result: ['apple', 'banana', 'cherry']
```

---

## 📝 Notes

- All methods **modify the original list**, except:
  - `copy()`
  - `count()`
  - `index()`
- Use `sorted()` or `reversed()` if you want a **new list**.
- For nested lists, use `copy.deepcopy()` to avoid shared references.

---
