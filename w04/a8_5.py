fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    if line.startswith("From: "):
        count += 1
        container = line.split()
        print(container[1])
print("There were", count, "lines in the file with From as the first word")
