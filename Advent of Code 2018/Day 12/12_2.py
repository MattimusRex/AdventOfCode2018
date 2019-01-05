with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

initial_state = lines[0][15:]
tests = set()
for line in lines[2:]:
    if line[9] == "#":
        tests.add(line[:5])

min_pot_index = 0
max_pot_index = 0
pots = set()
for i, entry in enumerate(initial_state):
    if entry == '#':
        pots.add(i)

gen = 0
while gen < 50000000000:
    if gen % 10000 == 0:
        print("#: " + str(len(pots)) + " Sum: " + str(sum(pots)) + " Gen: " + str(gen))
    temp_pots = set()
    checked = set()
    for pot in pots:
        for i in range(pot - 2, pot + 3):
            if i not in checked:
                checked.add(i)
                key = []
                for j in range(i - 2, i + 3):
                    if j in pots:
                        key.append("#")
                    else:
                        key.append(".")
                if ''.join(key) in tests:
                    temp_pots.add(i)
    pots = temp_pots
    gen += 1

print(sum(pots))
    
