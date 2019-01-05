import sys

total = 0
seen = set()
seen.add(total)
with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

while True:
    for line in lines:
        total += int(line)
        if total in seen:
            print(total)
            sys.exit()
        else:
            seen.add(total)