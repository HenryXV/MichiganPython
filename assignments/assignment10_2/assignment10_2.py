handle = open("mbox-short.txt")

counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5].split(":")
        counts[time[0]] = counts.get(time[0],0) + 1
for k,v in sorted(counts.items()):
    print(k,v)
