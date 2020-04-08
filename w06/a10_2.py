name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dictionary = dict()
for lines in handle:
    if lines.startswith("From "):
        line = lines.split()
        container = line[5]
        container = container.split(":")
        dictionary[container[0]] = dictionary.get(container[0], 0) + 1
for k, v in sorted(dictionary.items()):
    print(k, v)
