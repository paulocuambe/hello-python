name = "exercises/files/mbox-short.txt"

try:
    fhand = open(name)
except:
    exit(f"We had a problem opening the file named {name}")

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    [_, _, day, *_] = line.split()
    print(day)
