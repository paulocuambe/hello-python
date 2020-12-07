import string
fname = "exercises/dictionaries/romeo-full.txt"

try:
    fhand = open(fname)
except:
    exit(f"Could not open the file {fname}")

words = dict()
for line in fhand:
    line = line.rstrip().translate(line.maketrans('', '', string.punctuation))
    for word in line.lower().split():
        words[word] = words.get(word, 0) + 1

print(words)