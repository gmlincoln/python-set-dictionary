
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
### 📍 update() Items
#### 📍 Updating Existing Keys
- If a key already exists, update() overwrites the value.
##### Syntax 
```bash
    dictionary.update({key: value})

```
##### Code
```python
student = {"name": "Kafi", "age": 22}

student.update({"age": 23})

print(student)
# {'name': 'Kafi', 'age': 23}


```

#### If the key does not exist, update() adds it
```python
student = {
    "name": "Shuvo",
    "age": 22, 
    "city": "Dhaka"
    }
student.update({"cgpa": 3.90})

```
### 📍 Removing Items
#### Code
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


### 📍 6. Nested Dictionaries

####
```python
students = {
    "student1": {
        "name": "Tamim",
         "age": 22
         },
    "student2": {
        "name": "Nargis",
         "age": 23
    },
    "student3": {
        "name": "Shuvo",
         "age": 25
    },
    "student4": {
        "name": "Fairooz",
         "age": 21
    },

}
```
#####  Output
```bash

    #Tamim

```
### 📍 7. Dictionary Use Cases
#### ✔ 1. Storing real-world structured data

```python
user = {
    "id": 101,
    "name": "soikot",
    "email": "soikot@example.com"
}


```
#### 2. Using as a pseudo-database
```python
products = {
    101: {"name": "Laptop", "price": 50000},
    102: {"name": "Phone", "price": 20000}
}

```
####
```python


```
####
```python


```
####
```python


```

### 📍 8. Practice Questions
#### ✔ Basic
- Create a dictionary of 5 students with name and age.  
- Print all keys and values using loops.  
- Change the value of any key.

#### ✔ Intermediate
- Use update() to add multiple new fields.  
- Remove 2 items using pop() and del. 
- Create a nested dictionary and access nested values.

#### ✔ Advanced
- Count character frequency using a dictionary.  
- Convert two lists into a dictionary:  
-- Keys → Names  
-- Values → Marks  
- Write a program that stores employee details and retrieves them by user input ID.