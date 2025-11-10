# Python Syntax 2
## Outline
- [Built-in Data Structures](#sequence-types)
    - [List](#lists)
    - [Tuple](#tuples)
    - [Set](#set)
    - [Dictionary](#dictionary)
- [Control Flow](#flow-control)
    - If... else, while, for
- [Iterations](#iteration)

## Introduction
### Sequence Types
- Sequences are *containers* that hold objects
    - Built-in Python Data Structures
    - Finite, ordered, indexed by integers
- Tuple
    - An **immutable** ordered sequence of items
    - Items can be of mixed types, including collection types
- Strings
    - An **immutable** ordered sequence of chars
    - Conceptually very much like a tuple
- List
    - A **mutable** ordered sequence of items of mixed types
- Dictionary
    - A **mutable** ordered sequence of items with two elements (key and data) of mixed types
- Set
    - A **mutable** unordered sequence of items of mixed types without duplicated items

> Immutable: updating container will delete previous sequence address and declare it in a new address

## Lists
- Syntax: `[elem1, elem2, ...]`
- Ordered sequence of any type (mixed types ok)
- Mutable
```python
list1 = [1, 'hello', 4+2j, 123.12]
print(list1) # [1, 'hello', 4+2j, 123.12]

list1[0] = 'a'
print(list1) # ['a', 'hello', 4+2j, 123.12]
```
### Repeating
- Concatenation: list1 + list2
    ```python
    [1, 'a', 'b'] + [3, 4, 5]
    # [1, 'a', 'b', 3, 4, 5]
    ```
- Repetition: list * count
    ```python
    [23, 'x'] * 4
    # [23, 'x', 23, 'x', 23, 'x', 23 'x']
    ```

### Elements
- Append item to end
    - `list.append("elem")`
- Append another list
    - `list.extend(list2)`
- Insert item anywhere
    - `list.insert(index, "elem")`

### Removing Elements from a list
- Remove the first matching occurence of element (w/o returning it)
    - `list.remove("elem")`
    - Throws exception if argument is not in the list
- Remove last element and return it
    - `list.pop()`
- Remove by position
    - `list.pop([index])`
- Delete element by index
    - `del list[index]`
### Indexing
- Syntax: `list[n]`
- Positive indices count from the left: `list[0]`
- Negative indices count from the right: `list[-1]`

```py
list1 = ['a', 'b', 'c', 'd']
# list1[0] = list1[-4]
# list1[1] = list1[-3]
# list1[2] = list1[-2]
# list1[3] = list1[-4]
```

### List Slicing: get a sublist
- `list[m:n]`: return elements **m** up to **n** (exclusive)
- Syntax for both **strings** and **lists**

```py
x = [0, 1, 2, 3, 4, 5, 6, 7]

x[1:4] # [1, 2, 3]

x[2:-1] # [2, 3, 4, 5, 6]

# Missing Index means start or end of list
x[:2] # [0, 1]

"Hello nerd"[3:] # lo nerd
```

### Sorting a list
- `List.sort([comparator])`
    - Sort List in place. Result is applied to the list
    ```py
    list3 = [4, 12, 3, 9]
    list3.sort()
    print(list3) # [3, 4, 9, 12]
    ```

### Count or find elements in a list
- `list.count(element)`**
    - count number of occurences of element
- `n = list.index(element)`
    - return index of first occurence of element
    - Throws **ValueError** if element is not in list

## Tuples
- **Immutable** list
- Syntax: `(elem1, elem2, ...)`
- A tuple cannot be changed

```py
tuple1 = (1, 5, 10)
tuple1[2] = 2 # TypeError
```

### Converting between list and tuple
```py
list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
type(tuple1) # <class 'tuple'>

tuple2 = ('cat', 'dog')
list2 = list(tuple2)
type(list2) # <class 'list'>
```

### len - Length of an object
- `n = len(object)`
- Return the length of object
- len is **not** object-oriented
```py
list1 = [1, 2, 3, 4, 5]
print(len(list1)) # 5

string1 = "length of a string"
print(len(string1)) # 18
```

### Multiple assignment using tuples
- `(elem1, elem2, elem3) = (item1, item2, item3)`
- This can be used in for loops
```py
points = [[1,0,3], [0.2, 0.9, 0.4], [1,2,7]]
for [x,y,z] in points:
    r = math.hypot(x,y)
    print("radius of (%f, %f) is %f" % (x,y,r))
```

## Dictionary
- A **mapping** of keys to values
    - Associate a key with a value
    - Each key must be unique

- Syntax: `dict = {key1: val1, key2: val2, ...}`

```py
dict1 = {'a': 1, 'b': 2}
print(dict1) # {'a': 1, 'b': 2}

print(dict1['a']) # 1

print(dict1['b']) # 2

dict1[3] = 'three'
print(dict1) # {'a': 1, 'b': 2, 3: 'three'}
```

## Set
- An unordered collection, without duplicates (like Java)
- Syntax is like dictionary, but no ":" between key-value
    - `set = {elem1, elem2, ...}`

```py
aset = {'a', 'b', 'c'}
print(aset) # {'a', 'c', 'b'}
aset.add('c') # no effect, 'c' already in set
print(aset) # {'a', 'c', 'b'}
```

### Set Methods
- `set.discard('elem')`
    - remove element
    - No error if not in set
- `set.remove(elem')`
    - remove element
    - Error if not in set
- `set3 = set1.union(set2)`
    - doesn't change set1
- `set4 = set1.intersection(set2)`
    - doesn't change set1
- `set2.issubset(set1)`
    - is set2 a subset of set1
- `set2.issuperset(set1)`
    - is set2 a superset of set1
- `set2.difference(set1)`
    - element in set1 but not set2
- `set1.symmetric_difference(set2)`
    - xor
- `set1.clear()`
    - remove everything

### Test for element in Set
- `item in set`
```py
aset = {'a', 'b', 'c'}
'a' in aset # True
'A' in aset # False
```

## Flow Control
- if, elif, else
    ```py
    if condition:
        body
    elif condition2:
        body
    else:
        body
    ```
    ```py
    if x % 2 == 0:
        y = y + x
    else:
            y = y - x
    ```
- while loop
    ```py
    while condition:
        body
    ```
    ```py
    while count < 10:
        count = 2 * count
    ```
- for loop
    ```py
    for name in iterable:
        body
    ```
    ```py
    for x in [1,2,3]:
        sum = sum + x
    ```

### range: create a sequence
- `range([start,] stop[, step])`
- Generate a list of numbers from **start** to **stop**, stepping every **step**
- **start** defaults to 0, **step** defaults to 1
```py
range(5) # [0, 1, 2, 3, 4]

range(1, 9) # [1, 2, 3, 4, 5, 6, 7, 8]

range(2, 20, 5) # [2, 7, 12, 17]
```

### for loop using range()
- Use `range` to generate values to use in for loop
```py
for i in range (1, 4):
    print(i)

# 1
# 2
# 3
``` 

### loop iteration using continue
- skip to next iteration of a loop
```py
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# 1
# 3
# 5
# 7
# 9
```

### break
- break out of the inner-most loop
```py
for number in range(10):
    if number == 4:
        print("Breaking")
        break
    else:
        print(number)

# 0
# 1
# 2
# 3
# Breaking
```

## Iteration
- Most data structures can be iterated over in the same way
    ```py
    mylist = ['a', 'b', 'c']
    for item in mylist:
        print(item)
    ```
- Note we don't need the index of the element to access tuples
    ```py
    mytuple = ('a', 'b', 'c')
    for item in mytuple:
        print(item)
    ```
- When iterating over a dictionary, we iterate over the keys
    ```py
    mydict = {'a': 10, 'b': 15}
    for key in mydict:
        print(key, mydict[key])
    ```

- We can also iterate over indices
    ```py
    for i in range(4):
        print(i) # 0 1 2 3
    
    for i in range(1, 10, 2):
        print(i) # 1 3 5 7 9
    
    mylist = ['a', 'b', 'c']
    for i in range(len(mylist)):
        print(i, mylist[i])
        # 0 'a'
        # 1 'b'
        # 2 'c'
    
    for idx, item in enumerate(mylist):
        print(idx, item)
        # 0 'a'
        # 1 'b'
        # 2 'c'
    ```

## List Comprehensions
- Input: `nums = [1, 2, 3, 4, 5]`
- Goal: `sq_nums = [1, 4, 9, 16, 25]`
- Here's now we could already do this:
    ```py
    sq_nums = []
    for n in nums:
        sq_nums.append(n**2)
    ```
- Or... we could use comprehension:
    ```py
    sq_nums = [n ** 2 for n in  nums]
    # square brackets show we're making a list
    # apply some operation to the loop variable
    # loop over the specified iterable
    ```

### More List Comprehensions
- Template: `new_list = [f(x) for x in iterable]`

```py
words = ['hello', 'this', 'is', 'python']
caps = [word.upper() for word in words]

powers = [(x**2, x**3, x**4) for x in range(10)]
# Remember the iterable doesnt have to be a list
```

## Summary
- Built-in Data Structures
    - List
    - Tuple
    - Set
    - String
    - Dictionary
- Control Flow
    - If...else, while, for
- Iteration