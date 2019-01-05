import sys

class Elf:
    def __init__(self, index, dist):
        self.index = index
        self.dist = dist
        self.last_dir = None
    
    #moves down the path until a split
    def walk(self, string, elves):
        i = self.index
        while i < len(string):
            if string[i].isalpha():
                self.dist += 1
                if self.dist >= 1000:
                    global count 
                    count += 1
            elif string[i] == '(':
                elves = get_new_indexes(string, i, self.dist)
                return elves
            elif  string[i] == '|' or string[i] == ')':
                return
            i += 1


def get_new_indexes(string, start, dist):
    i = start + 1
    para_count = 1
    first = True
    elves = []
    while para_count > 0:
        if string[i] == '(':
            para_count += 1
        elif string[i] == ')':
            para_count -= 1
        elif string[i] == '|' and para_count == 1:
            first = True
        elif string[i].isalpha() and first:
            elves.append(Elf(i, dist))
            first = False
        i += 1
    #check for detour
    if string[i - 1] == '|':
        while not string[i].isalpha():
            i += 1
        elves.insert(0, Elf(i, dist))
    return elves




with open('input.txt', 'r') as inputFile:
    string = inputFile.readline()

# i = 14200
# while i < len(string):
#     print(string[i], end='')
#     i+=1
# sys.exit()


elves = []
elf = Elf(1, 0)
elves.append(elf)
count = 0
while len(elves) > 0:
    elf = elves.pop()
    print(f"elf starting at {elf.index} {string[elf.index]} {elf.dist}")
    new_elves = elf.walk(string, elves)
    if new_elves is not None:
        for e in new_elves:
            elves.append(e)

print(count)