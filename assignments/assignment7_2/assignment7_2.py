fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    fnumber = line[20:]
    total = total + float(fnumber)
    average = total / count

print('Average spam confidence:', average)
