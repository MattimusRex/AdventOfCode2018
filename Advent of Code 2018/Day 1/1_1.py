total = 0
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        total += int(line)
print(total)