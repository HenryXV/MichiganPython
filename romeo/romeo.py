handle = open("romeo.txt")

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigword = None
bigcount = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("The most common word in the play Romeo and Juliet is:", bigword, bigcount)
