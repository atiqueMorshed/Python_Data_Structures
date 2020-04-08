name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dictionary = dict()
for lines in handle:
    lines.rstrip()
    if lines.startswith("From "):
        line = lines.split()
        if len(line) >= 2:
            dictionary[line[1]] = dictionary.get(line[1], 0) + 1
value = None
key = None
for k, v in dictionary.items():
    if key is None or v > value:
        key = k
        value = v
print(key, value)
