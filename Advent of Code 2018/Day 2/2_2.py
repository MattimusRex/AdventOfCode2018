import sys
with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        error_index = None
        for k in range(len(lines[i])):
            if lines[i][k] != lines[j][k]:
                if error_index != None:
                    error_index = None
                    break
                else:
                    error_index = k
        if error_index is not None:
            print(lines[i][:error_index] + lines[i][error_index+1:])
            sys.exit()