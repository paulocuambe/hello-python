file_name = 'exercises/files/mbox-short.txt'
try:
    my_file = open(file_name)
except:
    exit("We had a problem opening the file" + file_name)

for line in my_file:
    if line.startswith('From:'):
        print(line.strip())
