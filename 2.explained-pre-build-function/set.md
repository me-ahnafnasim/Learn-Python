# 🔁 Set Methods in Python 🧠

In Python, a **set** is an unordered, mutable collection of unique elements. Sets are useful for operations like **removing duplicates**, **membership testing**, and performing **mathematical set operations** (like union, intersection, etc.).

---

## ✅ List of Common Set Methods

Here’s a complete list of **built-in methods for sets** in Python with simple explanations and examples.

---

### 1. `add()` ➕

**Adds an element to the end of the set**

```python
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}
```

---

### 2. `clear()` 🧹

**Removes all elements from the set**

```python
s = {1, 2, 3}
s.clear()
print(s)  # set()
```

---

### 3. `copy()` 💾

**Returns a shallow copy of the set**

```python
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)  # {1, 2, 3}
```

---

### 4. `difference()` ➖

**Returns the difference between two or more sets (elements in first set not in others)**

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))  # {1}
print(a-b)
```

---

### 5. `difference_update()` 🔄

**Removes items that exist in another set (modifies the original set)**

```python
a = {1, 2, 3}
b = {2, 3, 4}
a.difference_update(b)
print(a)  # {1}
```

---

### 6. `discard()` 🗑️

**Removes a specified element (no error if element is not found)**

```python
s = {1, 2, 3}
s.discard(2)
print(s)  # {1, 3}
```

> ⚠️ Unlike `remove()`, `discard()` does **not raise an error** if the item is not present.

---

### 7. `intersection()` 🔵🟡

**Returns a set containing the common elements of two or more sets**

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}
print(a & b)
```

---

### 8. `intersection_update()` 🔄

**Updates the set with the intersection of itself and another (modifies the original set)**

```python
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)  # {2, 3}
```

---

### 9. `isdisjoint()` ❓

**Returns `True` if two sets have no intersection**

```python
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True
```

---

### 10. `issubset()` 🔽

##### SUB = below / smaller / inside/ part of

##### SUPER = above / bigger / outside/ containing

**Returns `True` if another set contains this set**

```python
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True
```

---

### 11. `issuperset()` 🔼

**Returns `True` if this set contains another set**

```python
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # True
```

---

### 12. `pop()` 🧼

**Removes and returns an arbitrary element (since sets are unordered)**

```python
s = {1, 2, 3}
item = s.pop()
print("Removed:", item)
print("Updated set:", s)
```

> ⚠️ Since sets are **unordered**, you don't know which element will be popped.

---

### 13. `remove()` 🚫

**Removes a specific element (raises `KeyError` if not found)**

```python
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

s.remove(5)  # ❌ Raises KeyError
```

---

### 14. `symmetric_difference()` 🔁

**Returns a set with elements in either set, but not both**

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
```

---

### 15. `symmetric_difference_update()` 🔄

**Updates the set with symmetric differences (modifies the original set)**

```python
a = {1, 2, 3}
b = {3, 4, 5}
a.symmetric_difference_update(b)
print(a)  # {1, 2, 4, 5}
```

---

### 16. `union()` ∪

**Returns the union of sets (all unique elements)**

```python
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}
print(a|b)  # {1, 2, 3}
```

---

### 17. `update()` ➡️

**Updates the set with the union of another iterable/set (modifies the original set)**

```python
a = {1, 2}
a.update([2, 3, 4])
print(a)  # {1, 2, 3, 4}
```

---

## 📝 Summary Table

| Method                          | Description                           | Modifies Original? |
| ------------------------------- | ------------------------------------- | ------------------ |
| `add()`                         | Adds an element                       | ✅ Yes             |
| `clear()`                       | Removes all elements                  | ✅ Yes             |
| `copy()`                        | Returns a copy                        | ❌ No              |
| `difference()`                  | Returns set difference                | ❌ No              |
| `difference_update()`           | Updates set with difference           | ✅ Yes             |
| `discard()`                     | Removes element (no error if missing) | ✅ Yes             |
| `intersection()`                | Returns intersection                  | ❌ No              |
| `intersection_update()`         | Updates set with intersection         | ✅ Yes             |
| `isdisjoint()`                  | Checks if sets have no intersection   | ❌ No              |
| `issubset()`                    | Checks if set is subset               | ❌ No              |
| `issuperset()`                  | Checks if set is superset             | ❌ No              |
| `pop()`                         | Removes and returns arbitrary element | ✅ Yes             |
| `remove()`                      | Removes element (error if missing)    | ✅ Yes             |
| `symmetric_difference()`        | Returns symmetric difference          | ❌ No              |
| `symmetric_difference_update()` | Updates set with symmetric difference | ✅ Yes             |
| `union()`                       | Returns union                         | ❌ No              |
| `update()`                      | Updates set with union                | ✅ Yes             |

---
