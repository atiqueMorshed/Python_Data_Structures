fname = input("Enter file name: ")
fh = open(fname)
lst = list()
dir(lst)
for line in fh:
    container = line.rstrip()
    container = container.split()
    for obj in container:
        if obj not in lst:
            lst.append(obj)
lst.sort()
print(lst)
