fname = "exercises/files/mbox-short.txt"

try:
    fhand = open(fname)
except:
    exit(f"Could not open file {fname}")

emails = dict()
person = ""
nr_emails = 0
for line in fhand:
    if line.startswith("From "):
        email = line.rstrip().split()[1]
        emails[email] = emails.get(email, 0) + 1

        if emails[email] > nr_emails:
            person = email
            nr_emails = emails[email]

print(emails)
print(f"{person} sent {nr_emails}")