fname = 'romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for pieces in words:
        if pieces not in lst:
         lst.append(pieces)
print(sorted(lst))
