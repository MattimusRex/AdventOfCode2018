import sys
import math

def addr(registers, A, B, C):
    registers[C] = registers[A] + registers[B]

def addi(registers, A, B, C):
    registers[C] = registers[A] + B

def setr(registers, A, B, C):
    registers[C] = registers[A]

def seti(registers, A, B, C):
    registers[C] = A

def mulr(registers, A, B, C):
    registers[C] = registers[A] * registers[B]

def muli(registers, A, B, C):
    registers[C] = registers[A] * B

def gtrr(registers, A, B, C):
    if registers[A] > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

def gtir(registers, A, B, C):
    if A > registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

def eqrr(registers, A, B, C):
    if registers[A] == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

def eqri(registers, A, B, C):
    if registers[A] == B:
        registers[C] = 1
    else:
        registers[C] = 0

def bani(registers, A, B, C):
    registers[C] = registers[A] & B

def bori(registers, A, B, C):
    registers[C] = registers[A] | B

def line19(registers, A, B, C):
    registers[3] *= 256

def line18(registers, A, B, C):
    registers[3] = registers[5] + 1

def line17(registers, A, B, C):
    registers[5] = math.ceil(registers[4] / 256) - 1



def print_reg(registers):
     print(f" {instruction} {registers[0]:>12}, {registers[1]:>12}, {registers[2]:>12}, {registers[3]:>12}, {registers[4]:>12}, {registers[5]:>12}")

with open('input_2.txt', 'r') as input_file:
    instruction_pointer = input_file.readline()
    instructions = input_file.readlines()

instructions = [line.strip() for line in instructions]
instr_ptr_reg = int(instruction_pointer.split(' ')[1])
registers = [100000000000, 0, 0, 0, 0, 0]

i = 0
counter = 0
seen = set()
last = 0
while i < len(instructions):
    if i < 0 or i > len(instructions) - 1:
        break

    #write instruction pointer value to instruction register
    registers[instr_ptr_reg] = i

    #parse instruction
    instr_parts = instructions[i].split(' ')
    instruction = instr_parts[0]
    A = int(instr_parts[1])
    B = int(instr_parts[2])
    C = int(instr_parts[3])

    if i == 28:
        counter += 1
        if counter % 100 == 0:
            print (counter)
        if registers[1] not in seen:
            seen.add(registers[1])
            last = registers[1]
        else:
            print(last)
            sys.exit()


    #execute instruction
    if instruction == 'addi':
        addi(registers, A, B, C)
    elif instruction == 'addr':
        addr(registers, A, B, C)
    elif instruction == 'seti':
        seti(registers, A, B, C)
    elif instruction == 'setr':
        setr(registers, A, B, C)
    elif instruction == 'mulr':
        mulr(registers, A, B, C)
    elif instruction == 'muli':
        muli(registers, A, B, C)
    elif instruction == 'eqrr':
        eqrr(registers, A, B, C)
    elif instruction == 'eqri':
        eqri(registers, A, B, C)
    elif instruction == 'gtir':
        gtir(registers, A, B, C)
    elif instruction == 'gtrr':
        gtrr(registers, A, B, C)
    elif instruction == 'bani':
        bani(registers, A, B, C)
    elif instruction == 'bori':
        bori(registers, A, B, C)
    elif instruction == 'line17':
        line17(registers, A, B, C)
    elif instruction == 'line18':
        line18(registers, A, B, C)
    elif instruction == 'line19':
        line19(registers, A, B, C)
    elif instruction != 'skip':
        sys.exit(f"illegal operation {instruction}")


    i = registers[instr_ptr_reg]
    i += 1

print(counter)