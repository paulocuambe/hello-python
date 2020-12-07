fname = "exercises/files/mbox-short.txt"

try:
    fhand = open(fname)
except:
    exit(f"Could not open file {fname}")

emails = dict()
for line in fhand:
    if line.startswith("From "):
        email = line.rstrip().split()[1]
        emails[email] = emails.get(email, 0) + 1

print(emails)