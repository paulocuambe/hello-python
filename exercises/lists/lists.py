a = [13, 4, -2, 19, -17, 24, 5, 9, 18, 23, 35, 29]
b = [-3, 5, 17]
print(a)
print(b, end="\n\n")

# concatenate lists
join = a + b
print(sorted(join))
print(b * 2)  # Duplicate de list

brothers = ["Celeste", "Miranda", "Crimilda"]
brothers[1:1] = ["Osvaldo"]
print("\n", brothers)

brothers.extend(["All sons of God bought by the blood of Jesus Christ"])
print("\n", brothers)

del a[1:]
print(a)

print()

print(b.remove(17))  # None
print(b)  # [-3, 5]

print(b.pop(0))  # returns -3
print(b)  # [5]
