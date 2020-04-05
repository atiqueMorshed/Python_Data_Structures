fname = input("Enter file name: ")
fh = open(fname)
total = 0
c = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    total += float(line[20:])
    c += 1
print("Average spam confidence:", total/c)
