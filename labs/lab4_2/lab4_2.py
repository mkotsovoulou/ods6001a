# Open the file to read it
fh = open("mbox-short.txt")
emails = dict()
for line in fh:
    print(line.rstrip())
