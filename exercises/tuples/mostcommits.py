fname = "exercises/files/mbox-short.txt"

try:
    fhand = open(fname)
except:
    exit(f"Could not open file {fname}")

commit_count = dict()
for line in fhand:
    if line.startswith("From "):
        _, email, *_ = line.rstrip().split()
        commit_count[email] = commit_count.get(email, 0) + 1


def extract_commits(person):
    _, commits = person
    return commits


ls = list(commit_count.items())
ls.sort(key=extract_commits)

email, commits = ls.pop()
print(f"The person with most commits is {email} with {commits} total.")
