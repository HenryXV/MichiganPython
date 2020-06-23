handle = open("mbox-short.txt")

counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

key = None
value = None
for k,v in counts.items():
    if key is None or v > value:
        key = k
        value = v

print(key, value)
