"""
Write a function called chop that takes a list and modifies it, 
removing the first and last elements, and returns None.
"""


def chop(t):
    t.pop(1)
    t.pop()


a = [1, 2, 4, 5]

print(a)
chop(a)
print("After chop:")
print(a)