---
# 🟩 **Python Tuple – All Methods + Built-in Functions**

## ✔️ **Tuple Methods (Only 2 Methods!)**

Tuples have ONLY **two** built-in methods because they are **immutable**.
---

## 1️⃣ **`tuple.count(value)`**

Returns how many times a value appears in the tuple.

### **Example**

```python
t = (1, 2, 2, 3, 2)
print(t.count(2))   # Output: 3
```

---

## 2️⃣ **`tuple.index(value, start, end)`**

Returns the **first index** where the value appears.
Optional `start` and `end` behave like slicing.

### **Example**

```python
t = ('a', 'b', 'c', 'b')
print(t.index('b'))        # Output: 1
print(t.index('b', 2))     # Output: 3
```

---

# 🟧 **Built-in Functions That Work With Tuples**

These are NOT tuple methods but Python built-ins that work with any sequence (list, tuple, string…).

---

## 🔹 **`len()` – length of tuple**

```python
t = (10, 20, 30)
print(len(t))   # 3
```

---

## 🔹 **`max()` – largest element**

```python
t = (5, 9, 2)
print(max(t))   # 9
```

---

## 🔹 **`min()` – smallest element**

```python
t = (5, 9, 2)
print(min(t))   # 2
```

---

## 🔹 **`sum()` – sum of numeric elements**

```python
t = (1, 2, 3)
print(sum(t))   # 6
```

---

## 🔹 **`sorted()` – returns a _list_ (not tuple!)**

```python
t = (3, 1, 2)
print(sorted(t))   # [1, 2, 3]
```

---

## 🔹 **`tuple()` – convert to tuple**

```python
x = [1, 2, 3]
print(tuple(x))    # (1, 2, 3)
```

---

## 🔹 **`any()` – True if any element is True**

```python
t = (0, False, 5)
print(any(t))   # True  (because of 5)
```

---

## 🔹 **`all()` – True if all elements are True**

```python
t = (1, 2, 3)
print(all(t))   # True
```

---

## 🔹 **`enumerate()` – get index + value**

```python
t = ('a', 'b', 'c')
for idx, val in enumerate(t):
    print(idx, val)
```

---

## 🔹 **`in` keyword – membership test**

```python
t = (1, 2, 3)
print(2 in t)   # True
```

---

## 🔹 **`reversed()` – reverse iterator**

```python
t = (1, 2, 3)
print(tuple(reversed(t)))   # (3, 2, 1)
```

---

# 🟦 **Tuple Characteristics (Important for Exams)**

- Immutable → cannot change values after creation.
- Supports indexing & slicing.
- Allows duplicates.
- Can store different data types.
- Faster than lists (because immutable).
- Can be used as dictionary keys (if containing only hashable values).

---
