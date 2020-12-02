name = 'exercises/files/mbox-short.txt'

try:
    fhand = open(name)
except:
    exit("We had a problem opening the file named " + name)

total_confidence = 0
lines = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        _, confidence = line.strip().split()
        total_confidence += float(confidence)
        lines += 1

print(f"Average spam confidence: {total_confidence/lines}")