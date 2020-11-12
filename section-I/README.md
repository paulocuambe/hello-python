# Data Types

- Numbers
- String
- Lists
- Tuple
- Dictionary

## Numbers

Numbers in python are separated in 3 different types:

1. **Integers** - They can be of any length, they are only limited by the memory available. Ex: 1, 2, 532, 32328.
2. **Floating** - A floating-point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points. Ex: 1.0, 19.67, 3.14159265359.
3. **Complex** - Complex numbers are written in the form, `x + yj`, where x is the real part and y is the imaginary part. _I don't know if I'm going to need these right now, but I guess they are useful in Machine Learning stuff._ Ex: 1 + 2j.

# Strings

We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or """.

```py
my_string = "This is a string"
print(my_string)

my_other_string = '''This Is a mutiple lines
String. Well, I like to say Enjoy. So,
Enjoy My dear friends.'''
print(my_other_string)
```

# Lists

Lists contains a sequence of ordered items. The items in a list can have diferent types. Ex:

```py
my_list = [1, "element two", 9.82]
```

# Tuple

Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Once created cannot be modified.

Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically. They are defined within parentheses () where items are separated by commas. Ex:

```py
my_tuple = (1, 4, 7, "Paulo")
print(my_tuple[3])
```

## Python Set

Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered. Ex:

```py
my_set = {1, 2, 3, 5, "Kickstart"}
print(my_set)
```

We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.

```py
my_set2 = {1, 2, 3, 5, 5, 3, "Kickstart"}
print(my_set) // {1, 2, 3, 5, "Kickstart"}
```

The slicing operator [] does not work with set objects.

## Dictionary

Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.

```py
d = {1:'value','key':2}
```

We use key to retrieve the respective value. But not the other way around.

```py
d = {1:'value','key':2}
print(type(d))
print(d[1]);
print(d['key']);
```

This generates error, since that key does not exist in our dictionary.

```py
print("d[2] = ", d[2]);
```
