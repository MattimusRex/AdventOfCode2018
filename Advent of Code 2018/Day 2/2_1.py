twos = 0
threes = 0
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        counts = {}
        line = line.strip()
        two = False
        three = False
        for char in line:
            counts[char] = counts.get(char, 0) + 1
        for entry in counts:
            if counts[entry] == 2:
                two = True
            elif counts[entry] == 3:
                three = True
        if two:
            twos += 1
        if three:
            threes += 1

print(twos * threes)
