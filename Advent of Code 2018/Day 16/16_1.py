def addr(before, A, B, C):
    before[C] = before[A] + before[B]
    return before

def addi(before, A, B, C):
    before[C] = before[A] + B
    return before

def mulr(before, A, B, C):
    before[C] = before[A] * before[B]
    return before

def muli(before, A, B, C):
    before[C] = before[A] * B
    return before

def banr(before, A, B, C):
    before[C] = before[A] & before[B]
    return before

def bani(before, A, B, C):
    before[C] = before[A] & B
    return before

def borr(before, A, B, C):
    before[C] = before[A] | before[B]
    return before

def bori(before, A, B, C):
    before[C] = before[A] | B

def setr(before, A, B, C):
    before[C] = before[A]
    return before

def seti(before, A, B, C):
    before[C] = A
    return before

def gtir(before, A, B, C):
    if A > before[B]:
        before[C] = 1
    else:
        before[C] = 0
    return before

def gtri(before, A, B, C):
    if before[A] > B:
        before[C] = 1
    else:
        before[C] = 0
    return before

def gtrr(before, A, B, C):
    if before[A] > before[B]:
        before[C] = 1
    else:
        before[C] = 0
    return before

def eqir(before, A, B, C):
    if A == before[B]:
        before[C] = 1
    else:
        before[C] = 0
    return before

def eqri(before, A, B, C):
    if before[A] == B:
        before[C] = 1
    else:
        before[C] = 0
    return before

def eqrr(before, A, B, C):
    if before[A] == before[B]:
        before[C] = 1
    else:
        before[C] = 0
    return before


with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

i = 0
answer_counter = 0
while i < len(lines):
    before = []
    before.append(lines[i][9])
    before.append(lines[i][12])
    before.append(lines[i][15])
    before.append(lines[i][18])
    before = [int(x) for x in before]
    
    parts = lines[i+1].split()
    A = int(parts[1])
    B = int(parts[2])
    C = int(parts[3])

    after = []
    after.append(lines[i+2][9])
    after.append(lines[i+2][12])
    after.append(lines[i+2][15])
    after.append(lines[i+2][18])
    after = [int(x) for x in after]

    opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    
    opcode_counter = 0
    for opcode in opcodes:
        before_copy = [x for x in before]
        before_copy = opcode(before_copy, A, B, C)
        if before_copy == after:
            opcode_counter += 1

    if opcode_counter >= 3:
        answer_counter += 1

    i += 4

print(answer_counter)