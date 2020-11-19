numbers = []
strings = []

my_data = [
    1, 'one', 2, 'two', 'tree', 3, 4, 'four', 'five', 'six', 5, 6, 7, 'seven'
]

for element in my_data:
    if type(element) is str:
        strings.append(element)
    elif type(element) is int:
        numbers.append(element)

print(numbers, strings)