my_file = open('exercises/files/mbox-short.txt')

data = my_file.read()
print(len(data))
print()
print(data[:31])
print(len(my_file.read())) # 0

# count = 0
# for line in my_file:
#     count += 1

# print(count)
