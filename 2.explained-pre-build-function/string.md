### ✅ **Python String Methods Table**

| **Method**       | **Explanation**                                         | **Example**                                                 |
| ---------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| **upper()**      | Converts all characters to uppercase                    | `"hello".upper() → 'HELLO'`                                 |
| **lower()**      | Converts all characters to lowercase                    | `"HELLO".lower() → 'hello'`                                 |
| **title()**      | Converts first character of each word to uppercase      | `"hello world".title() → 'Hello World'`                     |
| **capitalize()** | Capitalizes first character of the string               | `"hello".capitalize() → 'Hello'`                            |
| **swapcase()**   | Swaps case (upper → lower, lower → upper)               | `"HeLLo".swapcase() → 'hEllO'`                              |
| **strip()**      | Removes whitespace (or specified chars) from both ends  | `" hello ".strip() → 'hello'`                               |
| **lstrip()**     | Removes whitespace (or specified chars) from left side  | `" hello".lstrip() → 'hello'`                               |
| **rstrip()**     | Removes whitespace (or specified chars) from right side | `"hello ".rstrip() → 'hello'`                               |
| **replace()**    | Replaces occurrences of a substring with another        | `"hello".replace('h','H') → 'Hello'`                        |
| **split()**      | Splits string into a list by delimiter                  | `"a,b,c".split(',') → ['a','b','c']`                        |
| **rsplit()**     | Splits from the right                                   | `"a,b,c".rsplit(',',1) → ['a,b','c']`                       |
| **splitlines()** | Splits string into list at line breaks                  | `"a\nb".splitlines() → ['a','b']`                           |
| **join()**       | Joins elements of iterable with the string as separator | `",".join(['a','b']) → 'a,b'`                               |
| **find()**       | Returns first index of substring (-1 if not found)      | `"hello".find('e') → 1`                                     |
| **rfind()**      | Returns last index of substring (-1 if not found)       | `"hello".rfind('l') → 3`                                    |
| **index()**      | Like `find()`, but raises error if not found            | `"hello".index('e') → 1`                                    |
| **rindex()**     | Like `rfind()`, but raises error if not found           | `"hello".rindex('l') → 3`                                   |
| **count()**      | Counts occurrences of a substring                       | `"hello".count('l') → 2`                                    |
| **startswith()** | Checks if string starts with given substring            | `"hello".startswith('he') → True`                           |
| **endswith()**   | Checks if string ends with given substring              | `"hello".endswith('lo') → True`                             |
| **isupper()**    | Returns True if all chars are uppercase                 | `"HELLO".isupper() → True`                                  |
| **islower()**    | Returns True if all chars are lowercase                 | `"hello".islower() → True`                                  |
| **istitle()**    | Returns True if string is in title case                 | `"Hello World".istitle() → True`                            |
| **isdigit()**    | Checks if all characters are digits                     | `"123".isdigit() → True`                                    |
| **isalpha()**    | Checks if all characters are letters                    | `"abc".isalpha() → True`                                    |
| **isalnum()**    | Checks if all characters are letters or digits          | `"abc123".isalnum() → True`                                 |
| **isspace()**    | Checks if all characters are whitespace                 | `"   ".isspace() → True`                                    |
| **zfill()**      | Pads string with zeros to the left to fill width        | `"7".zfill(3) → '007'`                                      |
| **center()**     | Centers string in given width, fills with spaces        | `"hi".center(5,'-') → '--hi-'`                              |
| **ljust()**      | Left-align string in given width                        | `"hi".ljust(5,'-') → 'hi---'`                               |
| **rjust()**      | Right-align string in given width                       | `"hi".rjust(5,'-') → '---hi'`                               |
| **format()**     | Formats string with placeholders                        | `"{0} {1}".format('Hi','There') → 'Hi There'`               |
| **format_map()** | Like format(), but takes a dict directly                | `"{x} {y}".format_map({'x':'Hi','y':'There'}) → 'Hi There'` |
| **encode()**     | Encodes string to bytes                                 | `"hello".encode() → b'hello'`                               |
| **expandtabs()** | Replaces `\t` with spaces                               | `"a\tb".expandtabs(4) → 'a   b'`                            |
| **partition()**  | Splits at first occurrence of separator into 3 parts    | `"a=b".partition('=') → ('a','=','b')`                      |
| **rpartition()** | Splits at last occurrence of separator into 3 parts     | `"a=b=c".rpartition('=') → ('a=b','=','c')`                 |

---

---

---

## REPLACE()-------------------------------------------

---

```markdown
"""
What is .replace()?
The .replace() method returns a new string where all occurrences
(or a specific number) of a substring are replaced with another substring.

🔁 Strings in Python are immutable, so .replace() does not change the original string
— it returns a new one.

string.replace(old, new, count)
count → (Optional) Maximum number of replacements to make
"""
```

- `old`: The substring you want to replace.
- `new`: The substring to replace with.
- `count` _(Optional)_: The maximum number of replacements to make.

---

## 🔹 Examples

### 1️⃣ Basic Replacement

```python
text = "I love apples. Apples are delicious. I eat apples every day."
new_text = text.replace("apples", "oranges")
print(new_text)
```

**Output:**

```
I love oranges. Apples are delicious. I eat oranges every day.
```

❌ **Why didn't "Apples" change?**
Because `.replace()` is **case-sensitive**!

---

### 2️⃣ Limit Number of Replacements with `count`

```python
text = "cat, cat, dog, cat, bird"
result = text.replace("cat", "mouse", 2)
print(result)
```

**Output:**

```
mouse, mouse, dog, cat, bird
```

Only the **first 2** `"cat"` occurrences were replaced.

---

### 3️⃣ Remove a Substring (Replace with Empty String)

```python
text = "Hello, World!"
clean = text.replace(",", "")
print(clean)
```

**Output:**

```
Hello World!
```

---

### 4️⃣ Replace Whitespace or Special Characters

```python
name = "John\nDoe\tAge:25"
clean = name.replace("\n", " ").replace("\t", " ")
print(clean)
```

**Output:**

```
John Doe Age:25
```

---

### 5️⃣ Replace Space with Underscore

```python
text = "hello world"
new_text = text.replace(" ", "_")
print(new_text)
```

**Output:**

```
hello_world
```

---

✅ Use `.replace()` when:

- You want to substitute characters or substrings.
- You need to clean or format strings.
- You want to limit replacements using `count`.

🔒 Remember: The original string is never modified — `.replace()` always returns a **new** one!

---

---

## --------------------------------STRIP()-------------------------------------

---

The `.strip()` method in Python is used to **remove leading and trailing characters** from a string — most commonly **whitespace** (spaces, tabs, newlines) by default.

---

## ✅ **Basic Usage**

```python
string.strip([chars])
```

- **`chars`** _(optional)_: A string specifying the set of characters to remove.
- If `chars` is **not provided**, it removes **spaces**, `\n`, `\t`, etc. from both ends.
- It **does not affect** characters in the middle of the string.
- It returns a **new string** (strings are immutable).

---

## 🔹 **Examples**

### 1️⃣ **Remove Whitespace (Default Behavior)**

```python
text = "   Hello, World!   "
print(text.strip())
```

**Output:**

```
Hello, World!
```

---

### 2️⃣ **Remove Newline (`\n`) and Tab (`\t`)**

```python
text = "\n\t  Python is fun\t\n"
print(text.strip())
```

**Output:**

```
Python is fun
```

---

### 3️⃣ **Remove Specific Characters**

```python
text = "!!##Welcome!!"
print(text.strip("!#"))
```

**Output:**

```
Welcome
```

🔸 All `!` and `#` are removed from **both ends**.

---

### 4️⃣ **Only from Ends – Not Middle**

```python
text = "!!Good!Morning!!"
print(text.strip("!"))
```

**Output:**

```
Good!Morning
```

Notice `!` in the **middle** remains untouched.

---

## 🧠 Related Methods

| Method      | Description                                |
| ----------- | ------------------------------------------ |
| `.strip()`  | Removes characters from **both ends**      |
| `.lstrip()` | Removes characters from the **left/start** |
| `.rstrip()` | Removes characters from the **right/end**  |

---

---

---

## JOIN()

---

In Python, the `.join()` method is used to **combine a list (or any iterable) of strings into a single string**, with a specified separator between each element.

---

### 🔧 **Syntax**

```python
separator.join(iterable)
```

- `separator`: The string you want to place **between** each element (e.g., `" "`, `","`, `"-"`).
- `iterable`: A list, tuple, or any iterable **containing strings**.

---

### ✅ **Examples**

| Code                             | Output          | Explanation      |
| -------------------------------- | --------------- | ---------------- |
| `" ".join(["hello", "world"])`   | `'hello world'` | Joins with space |
| `"-".join(["2025", "08", "07"])` | `'2025-08-07'`  | Joins with dash  |
| `"".join(["a", "b", "c"])`       | `'abc'`         | No separator     |
| `",".join(["1", "2", "3"])`      | `'1,2,3'`       | Joins with comma |

---

### ❗ Important Notes

- All elements in the iterable **must be strings**. If you have integers, use `str()` or `map()` to convert:

```python
nums = [1, 2, 3]
"-".join(map(str, nums))  # '1-2-3'
```

---

### 📌 Real-world Example

```python
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome
```
