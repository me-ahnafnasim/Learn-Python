# Python Dictionary Methods (VS Code Note)

This note provides a comprehensive overview of commonly used dictionary methods in Python.

---

## 1. `clear()`

- **Purpose:** Removes all items (key-value pairs) from the dictionary.
- **Returns:** `None`
- **Example:**
  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  my_dict.clear()
  print(my_dict)  # Output: {}
  ```

---

## 2. `copy()`

- **Purpose:** Returns a **shallow copy** of the dictionary. Changes to the copied dictionary will not affect the original, but if the dictionary contains mutable objects (like lists), changes to those nested objects will be reflected in both.
- **Returns:** A new dictionary that is a shallow copy.
- **Example:**
  ```python
  original_dict = {'a': 1, 'b': [2, 3]}
  copied_dict = original_dict.copy()
  copied_dict['a'] = 100
  copied_dict['b'].append(4)
  print(original_dict) # Output: {'a': 1, 'b': [2, 3, 4]}
  print(copied_dict)   # Output: {'a': 100, 'b': [2, 3, 4]}
  ```

---

## 3. `fromkeys(iterable, value=None)`

- **Purpose:** Creates a new dictionary with keys from `iterable` and values set to `value`. If `value` is not provided, it defaults to `None`.
- **Returns:** A new dictionary.
- **Example:**

  ```python
  keys = ['name', 'age', 'city']
  new_dict = dict.fromkeys(keys)
  print(new_dict) # Output: {'name': None, 'age': None, 'city': None}

  new_dict_with_value = dict.fromkeys(keys, 'unknown')
  print(new_dict_with_value) # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
  ```

---

## 4. `get(key, default=None)`

- **Purpose:** Returns the value for the specified `key`. If `key` is not found, it returns `default` (which is `None` by default), instead of raising a `KeyError`.
- **Returns:** The value associated with the key, or the default value if the key is not found.
- **Example:**
  ```python
  my_dict = {'name': 'Alice', 'age': 30}
  print(my_dict.get('name'))     # Output: Alice
  print(my_dict.get('city'))     # Output: None
  print(my_dict.get('city', 'New York')) # Output: New York
  ```

---

## 5. `items()`

- **Purpose:** Returns a **new view** of the dictionary's items (key-value pairs) as tuples. The view object will reflect any changes made to the dictionary.
- **Returns:** A view object.
- **Example:**

  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  items_view = my_dict.items()
  print(items_view) # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

  for key, value in items_view:
      print(f"{key}: {value}")
  ```

---

## 6. `keys()`

- **Purpose:** Returns a **new view** of the dictionary's keys. The view object will reflect any changes made to the dictionary.
- **Returns:** A view object.
- **Example:**

  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  keys_view = my_dict.keys()
  print(keys_view) # Output: dict_keys(['a', 'b', 'c'])

  for key in keys_view:
      print(key)
  ```

---

## 7. `pop(key, default=NoDefault)`

- **Purpose:** Removes the item with the specified `key` and returns its corresponding value. If `key` is not found and `default` is not provided, it **raises a `KeyError`**. If `default` is provided, it returns `default` instead.
- **Returns:** The value associated with the removed key, or the default value.
- **Example:**

  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  value_b = my_dict.pop('b')
  print(value_b)  # Output: 2
  print(my_dict)  # Output: {'a': 1, 'c': 3}

  # Handling missing key with a default value
  value_d = my_dict.pop('d', 'Key not found')
  print(value_d)  # Output: Key not found

  # This would raise a KeyError if 'e' is not present and no default is provided
  # value_e = my_dict.pop('e')
  ```

---

## 8. `popitem()`

- **Purpose:** Removes and returns a (key, value) pair from the dictionary. In Python 3.7+, `popitem()` removes the **last inserted item**. In earlier versions, it removed an arbitrary item. Raises a `KeyError` if the dictionary is empty.
- **Returns:** A (key, value) tuple.
- **Example:**
  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  item1 = my_dict.popitem()
  print(item1)  # Output: ('c', 3) (or an arbitrary item in older Python)
  print(my_dict) # Output: {'a': 1, 'b': 2}
  ```

---

## 9. `setdefault(key, default=None)`

- **Purpose:** Returns the value of the `key` if `key` is in the dictionary. If `key` is not found, it **inserts `key` with the `default` value** (which is `None` by default) into the dictionary and returns that `default` value.
- **Returns:** The value associated with the key, or the default value if the key was newly inserted.
- **Example:**

  ```python
  my_dict = {'name': 'Bob'}
  name = my_dict.setdefault('name', 'Unknown')
  print(name)   # Output: Bob
  print(my_dict) # Output: {'name': 'Bob'}

  age = my_dict.setdefault('age', 25)
  print(age)    # Output: 25
  print(my_dict) # Output: {'name': 'Bob', 'age': 25}
  ```

---

## 10. `update([other])`

- **Purpose:** Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs. If a key already exists, its value is updated; otherwise, new key-value pairs are added.
- **Returns:** `None`
- **Example:**

  ```python
  dict1 = {'a': 1, 'b': 2}
  dict2 = {'b': 3, 'c': 4}
  dict1.update(dict2)
  print(dict1) # Output: {'a': 1, 'b': 3, 'c': 4}

  dict1.update([('d', 5), ('e', 6)])
  print(dict1) # Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
  ```

---

## 11. `values()`

- **Purpose:** Returns a **new view** of the dictionary's values. The view object will reflect any changes made to the dictionary.
- **Returns:** A view object.
- **Example:**

  ```python
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  values_view = my_dict.values()
  print(values_view) # Output: dict_values([1, 2, 3])

  for value in values_view:
      print(value)
  ```

---
