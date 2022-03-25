# Open the file to read it
fh = open("datafile.txt")
words = list()
for line in fh:
    print(line.rstrip())
