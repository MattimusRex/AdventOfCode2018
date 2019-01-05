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
    return before

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


with open('input_2.txt', 'r') as inputFile:
    lines = inputFile.readlines()

i = 0
opcodes = [gtrr, borr, gtir, eqri, addr, seti, eqrr, gtri, banr, addi, setr, mulr, bori, muli, eqir, bani]
registers = [0, 0, 0, 0]

while i < len(lines):
    parts = lines[i].split()
    A = int(parts[1])
    B = int(parts[2])
    C = int(parts[3])
    opcode_num = int(parts[0])
    
    registers = opcodes[opcode_num](registers, A, B, C)
    i += 1

print(registers[0])
