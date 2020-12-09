"""
Print the 10 words with more occurences in the text. Make sure to exclude all the puntuation
signs in the text.
https://www.py4e.com/code3/romeo-full.txt
"""
import string
fname = "exercises/dictionaries/romeo-full.txt"

try:
    fhand = open(fname)
except:
    exit(f"Could not open the file {fname}")

# Count all words
words = dict()
for line in fhand:
    # remove all pontuaction from the line
    line = line.rstrip().translate(line.maketrans('', '', string.punctuation))
    for word in line.lower().split():
        words[word] = words.get(word, 0) + 1

# convert dictionary to list of tuple (word, nr)
lst = list(words.items())


# extract the nr of repitition from the tuple
def nr_repetitions(word):
    _, rep = word
    return rep


# sort by nr of repitition in descending order
lst.sort(key=nr_repetitions, reverse=True)
for word, nr in lst[:10]:
    print(word, nr)