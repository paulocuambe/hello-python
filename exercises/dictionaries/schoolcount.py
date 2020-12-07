fname = "exercises/files/mbox-short.txt"

try:
    fhand = open(fname)
except:
    exit(f"Could not open file {fname}")

schools = dict()
for line in fhand:
    if line.startswith("From "):
        at_pos = line.find("@")
        sp_pos = line.find(" ", at_pos)
        school = line[at_pos + 1:sp_pos]

        schools[school] = schools.get(school, 0) + 1

print(schools)