"""
  Then write a function called middle that takes a list and returns a 
  new list that contains all but the first and last elements.
"""


def middle(t):
    [_, *m, _] = t
    return m


a = [1, 2, 3, 4, 5, 6]
print(a)
print("After middle")
print(a)
print("Middle:")
print(middle(a))