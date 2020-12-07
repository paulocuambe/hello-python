fname = "exercises/files/mbox-short.txt"

try:
    fhand = open(fname)
except:
    exit(f"Could not open file {fname}")

days = dict()
for line in fhand:
    if line.startswith("From "):
        week_day = line.rstrip().split()[2]
        days[week_day] = days.get(week_day, 0) + 1

print(days)