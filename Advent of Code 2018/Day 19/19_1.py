import sys

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

def eqrr(registers, A, B, C):
    if registers[A] == registers[B]:
        registers[C] = 1
    else:
        registers[C] = 0

with open ('input.txt', 'r') as inputFile:
    instruction_pointer = inputFile.readline()
    instructions = inputFile.readlines()

instr_ptr_reg = int(instruction_pointer.split(' ')[1])
instructions = [line.strip() for line in instructions]
registers = [0, 0, 0, 0, 0, 0]

i = 0
counter = 0
while i < len(instructions):
    # counter += 1
    # if counter % 100 == 0:
    #     print(counter)

    if i < 0 or i > len(instructions) - 1:
        break

    #write instruction pointer value to instruction register
    registers[instr_ptr_reg] = i

    if registers[2] > 1:
        print(f"{registers[0]:>10}, {registers[1]:>10}, {registers[2]:>10}, {registers[3]:>10}, {registers[4]:>10}, {registers[5]:>10}")
        sys.exit()

    #parse instruction
    instr_parts = instructions[i].split(' ')
    instruction = instr_parts[0]
    A = int(instr_parts[1])
    B = int(instr_parts[2])
    C = int(instr_parts[3])

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
    elif instruction == 'gtrr':
        gtrr(registers, A, B, C)
        
    #write instruction register value back to instruction pointer
    i = registers[instr_ptr_reg]
    i += 1

print(registers[0])
