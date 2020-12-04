fname = "exercises/dictionaries/words.txt"

try:
  fhand = open(fname)
except:
  exit(f"Could not open the file {fname}")

word_dict = dict()
for line in fhand:
  for word in line.split():
    if word in word_dict: continue
    word_dict[word] = 3

print(word_dict)