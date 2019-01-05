with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

initial_state = lines[0][15:]
tests = set()
for line in lines[2:]:
    if line[9] == "#":
        tests.add(line[:5])

overflow = 1000

pots = ["."] * overflow
for char in initial_state.strip():
    pots.append(char)

for i in range(overflow):
    pots.append(".")

gen = 0
while gen < 20:
    temp = [".", "."]
    for i in range(2, len(pots) - 2):
        #print(''.join(pots[i-2:i+3]))
        if ''.join(pots[i-2:i+3]) in tests:
            temp.append("#")
        else:
            temp.append(".")
    temp.append(".")
    temp.append(".")
    pots = temp
    gen += 1

total = 0
for i, pot in enumerate(pots):
    if pot == "#":
        total += (i - overflow)
    
print(total)