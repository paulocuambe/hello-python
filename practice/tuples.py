my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
second_tuple = "Mabassa", "Kirro", "Juyria"

print(my_tuple, second_tuple)
print(type(my_tuple), type(second_tuple))

print(my_tuple[2:])  # Prints from number 3 on
print(my_tuple[1:6])  # Prints from number 2 on to 6

# duplicates de content of the tuple Mabassa...Juyria, Mabassa...Juyria
tmp = second_tuple * 2
print(tmp)

# Trows TypeError: 'tuple' object does not support item assignment
my_tuple[3] = 2
"""
  Tuples are read only, but you can reassign the variable a new values.
  If this is not clear yet, I mean that you can not override a value stored in any position of the tuple, because it is read only.
  But as python is a dynamic language, you can take that variable and give it a new type/data.
"""
my_tuple = 2
print(my_tuple)  # Prints 2
