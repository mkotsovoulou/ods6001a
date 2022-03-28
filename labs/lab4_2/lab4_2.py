# Open the file to read it
fh = open("2021-07-08_clean-hashtags.tsv")
coronavirustags = dict()
for line in fh:
    print(line.rstrip())
