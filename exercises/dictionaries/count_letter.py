"""
Count how many times each letter appears in a string.
"""

word = "lollipop"
# Traditional way
trad_count = dict()
for l in word:
    if l not in trad_count:
        trad_count[l] = 1
    else:
        trad_count[l] += 1
print(trad_count)

# An elegant way
elegant_count = dict()
for l in word:
    elegant_count[l] = elegant_count.get(l, 0) + 1
print(trad_count)