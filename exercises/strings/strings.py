friend = "JESUS"
fruit = "banana"
singer = "Alessandro Vilas Boas"

print(len(fruit))  # 6
print(fruit[2:])  # nana
print(fruit[-2])  # n
print()

# Looping the string
for char in friend:
    print(char)

print()
# you can reverse the string this way - friend_reversed = reversed(friend)
for char in friend[::1]:
    print(char)

print(dir(singer))  # Printy all methods
print()
# removes empty spaces from the beginning and end
print("  some radom text with weird spacing   ".strip())
print()
print(singer.count("a"))