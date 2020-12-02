file_name = "exercises/lists/romeo.txt"

try:
    fhand = open(file_name)
except:
    exit(f"Could not open the file {file_name}")

words = []
for line in fhand:
    for word in line.rstrip().split():
        if word in words: continue
        words.append(word)

words.sort()
print(words)