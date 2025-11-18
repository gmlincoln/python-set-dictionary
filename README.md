# 📘 Python Tuple

## 🧠 What is a Tuple?
A **tuple** in Python is a collection of items that is:

- **Ordered**
- **Immutable** (cannot be changed after creation)
- Allows **duplicate values**
- Can store **multiple data types**

Tuples are written using **parentheses `( )`**.

### Example
```python
my_tuple = (10, 20, 30)
print(my_tuple)
```

### ✨ Why Use Tuples?
- Faster than lists  
- Data remains safe because tuples cannot be changed  
- Can be used as dictionary keys  
- Good for fixed data  

### 📍 1. Creating Tuples
#### ✔ Normal Tuples
```python
numbers = (1, 2, 3, 4)
```

#### ✔ Tuple with multiple data types

```python
student = ("Rahim", 21, 3.75, True)
```

#### ✔ Tuple without parentheses (tuple packing)
```python
fruits = "apple", "mango", "banana"

```

#### ✔ Single-item Tuple (Important)
```python
single = (10,)       # Correct
not_tuple = (10)     # Wrong → This is an integer

```

### 📍 2. Accessing Tuple Items
#### ✔ Access by index
```python
numbers = (10, 20, 30, 40)
print(numbers[0])   # 10
print(numbers[2])   # 30

```
#### ✔ Negative indexing
```python
print(numbers[-1])  # 40
print(numbers[-2])  # 30

```


### 📍 3. Slicing Tuples
####
```python
letters = ('a', 'b', 'c', 'd', 'e')

print(letters[1:4])   # ('b', 'c', 'd')
print(letters[:3])    # ('a', 'b', 'c')
print(letters[2:])    # ('c', 'd', 'e')

``` 
### 📍 4. Looping Through Tuples
#### ✔ Using for loop
```python
colors = ("red", "green", "blue")

for c in colors:
    print(c)

```
#### ✔ Using index

```python
for i in range(len(colors)):
    print(colors[i])

```

### 📍 5. Useful Tuple Methods
#### ✔ count()
Counts how many times a value appears.

```python
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))   # 3

```
#### ✔ index()
Returns the index of the first occurrence.

```python
print(numbers.index(3))   # 2

```
### 📍 6. Tuple Unpacking
#### ✔ Basic Unpacking
```python
person = ("Rafi", 25, "Dhaka")

name, age, city = person

print(name)  # Rafi
print(age)   # 25
print(city)  # Dhaka

```
#### ✔ Using * (Star) for multiple values
```python
values = (10, 20, 30, 40, 50)

a, b, *rest = values

print(a)     # 10
print(b)     # 20
print(rest)  # [30, 40, 50]

```



###  📍 7. Tuple vs List (Quick Comparison) 

| Feature    | Tuple      | List         |
| ---------- | ---------- | ------------ |
| Syntax     | `( )`      | `[ ]`        |
| Changeable | ❌ No       | ✅ Yes        |
| Faster     | ✅ Yes      | ❌ No         |
| Used For   | Fixed data | Dynamic data |

### 📍 8. Practical Examples
#### ✔ Example 1: Return multiple values from a function
```python 
def calculate(a, b):
    return (a + b, a * b)

sum_result, mul_result = calculate(10, 5)

print(sum_result)  # 15
print(mul_result)  # 50

```
#### ✔ Example 2: List of tuples (student records)
```python
 students = [
    ("Shuvo", 24),
    ("Fairoz", 23),
    ("Tamim", 22),
    ("Sayem", 25)
]

```

### 📍 9. Practice Questions
#### ✔ Basic
- Create a tuple with 5 items and print each item.  
- Create a tuple of numbers and find the sum.   
- Print the last item of a tuple using negative indexing.  

#### ✔ Intermediate
- Slice a tuple to get the middle three items.  
- Count how many times a value appears in a tuple.  
- Unpack a tuple into 4 variables.
  
#### ✔ Advanced
- Write a function that returns (min_value, max_value) without using min() or max().  
- Store multiple student records using a list of tuples and print only the names.  
- Modify the tuple value using index number [you can search it]




# 📘 Python Set

## 🧠 What is a Set?
A **set** in Python is a **collection of unique items** that is:

- **Unordered** (no indexing)  
- **Mutable** (can add or remove items)  
- **No duplicate values allowed**  

Sets are written using **curly braces `{ }`** or the `set()` function.

#### Example
```python
my_set = {1, 2, 3, 4}
```

### ✨ Why Use Sets?
- Automatically removes duplicates  
-Efficient for membership tests  
-Useful for mathematical operations like union, intersection  

### 📍 1. Creating Sets
#### ✔ Using curly braces
```python
fruits = {"apple", "banana", "mango"}
print(fruits)
```

#### ✔ Using set() function
```python
numbers = set([1, 2, 3, 4])
print(numbers)
```


#### ✔ Empty set (important!)
```python
empty_set = set()    # Correct
empty_set = {}       # Wrong → This creates a dictionary
```

### 📍 2. Accessing Set Items

Since sets are unordered, you cannot access items by index.
You can loop through items:

#### 📍 3. Adding and Removing Items

```python
fruits = {"apple", "banana"}
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'mango'}

```
#### ✔ Add multiple items
```python
fruits = {"apple", "banana"}
fruits.update(["grape", "orange"])
print(fruits)  # {'apple', 'banana', 'mango', 'grape', 'orange'}

```
#### ✔ Remove items
```python
fruits = {'apple', 'banana', 'mango', 'grape', 'orange'}
fruits.remove("banana")  # KeyError if item not found
fruits.discard("banana") # No error if item not found

```
#### ✔ Remove random item
```python

fruits.pop()  # Removes a random item

```
#### ✔ Clear all items
```python

fruits.clear()
print(fruits)
```
### 📍 4. Set Methods

####


| Method                   | Description                                  |
| ------------------------ | -------------------------------------------- |
| `add()`                  | Add single item                              |
| `update()`               | Add multiple items                           |
| `remove()`               | Remove specific item (error if not found)    |
| `discard()`              | Remove specific item (no error if not found) |
| `pop()`                  | Remove a random item                         |
| `clear()`                | Remove all items                             |
| `union()`                | Combine two sets (duplicates removed)        |
| `intersection()`         | Items present in both sets                   |
| `difference()`           | Items in first set but not in second         |
| `symmetric_difference()` | Items in one set or other but not both       |
| `copy()`                 | Returns a copy of the set                    |


##### ✔ Examples
```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))                # {1, 2, 3, 4, 5}
print(a.intersection(b))         # {3}
print(a.difference(b))           # {1, 2}
print(a.symmetric_difference(b)) # {1, 2, 4, 5}

```
### 📍 5. Set Use Cases
#### 5.1 Remove duplicates from a list
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}

```
#### 5.2 Membership testing
```python
fruits = {"apple", "banana", "mango"}
print("apple" in fruits)  # True
print("grape" in fruits)  # False

```
#### 5.3 Mathematical operations 
```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))         # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1, 2}

```
#### 5.4 Removing duplicates in real-life data
- User IDs  
- Email lists  
- Product SKUs
  
```python

```
#### 
```python

```
#### 
```python

```



### 📍 6. Practice Questions
#### ✔ Basic
- Create a set of 5 fruits and print it.  
- Check if an item exists in a set.  
- Add and remove items from a set.

#### ✔ Intermediate
- Remove duplicates from a list using a set.
- Find union, intersection, and difference of two sets.  
- Loop through a set and print each item.

#### ✔ Advanced
- Find items present in one set but not in another using symmetric_difference().
- Copy a set and modify the copy without changing the original.



# 📘  Dictionary 

## 🧠 What is a Dictionary?
A **dictionary** in Python is a collection of data stored in **key–value pairs**.

- **Ordered** (Python 3.7+)
- **Mutable** (can change items)
- **No duplicate keys**
- Values can be any data type

Dictionaries are written using **curly braces `{ }`**.

### Example
```python
student = {
    "name": "Rodri",
    "age": 22,
    "city": "Dhaka"
}
```


### 📍 1. Creating Dictionaries
#### ✔ Basic dictionary
```python
person = {
    "name": "John",
    "age": 30
}

```

#### ✔ Using dict() constructor
```python
person = dict(name="John", age=30)
```


#### ✔ Empty dictionary
```python
empty_dict = {}
```
### 📍 2. Accessing and Updating Values
#### ✔ Access using key

```python

student = {
    "name": "Karina", 
    "dept": "CSE"
}
print(student["name"])  # Karina

```

#### ✔ Using get() (avoids KeyError)

```python
print(student.get("dept"))       # CSE
print(student.get("CGPA", "N/A")) # N/A (default value)

```

#### ✔ Add or update value

```python
student["cgpa"] = 3.92
student["name"] = "Tamim"

```
### 📍 3. Removing Items
####
```python
student = {
    "name": "Shuvo",
    "age": 22, 
    "city": "Dhaka"
    }


```



####  ✔ pop()
```python

student.pop("age")  # removes age key

```
#### ✔ popitem() – removes last item
```python
student.popitem()


```
#### ✔ clear()
```python
 student.clear()

```


### 📍 4. Looping Through Dictionary
#### ✔ Loop keys
```python
for key in student:
    print(key)

```


#### ✔ Loop values
```python
for value in student.values():
    print(value)


```
#### ✔ Loop both key and value
```python
for key, value in student.items():
    print(key, value)

```

### 📍 5. Dictionary Methods

| Method         | Description                                            |
| -------------- | ------------------------------------------------------ |
| `get()`        | Returns value for key or default                       |
| `keys()`       | Returns all keys                                       |
| `values()`     | Returns all values                                     |
| `items()`      | Returns key–value pairs                                |
| `update()`     | Updates dictionary                                     |
| `pop()`        | Removes item by key                                    |
| `popitem()`    | Removes last inserted item                             |
| `clear()`      | Removes all items                                      |
| `copy()`       | Returns a shallow copy                                 |
| `setdefault()` | Returns value; if key not found, adds key with default |


####
```python


```