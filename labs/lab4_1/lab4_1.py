# Open the file to read it
fh = open("datafile.txt")
lst = list()
for line in fh:
    print(line.rstrip())
