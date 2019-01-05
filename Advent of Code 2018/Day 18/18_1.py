
def process(grid):
    temp = []
    for i in range(size):
        row = [0] * size
        temp.append(row)
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            trees, lumberyards = get_adjacent((i, j), grid)
            if col == '.':
                if trees > 2:
                    temp[i][j] = '|'
                else:
                    temp[i][j] = '.'
            elif col == '|':
                if lumberyards > 2:
                    temp[i][j] = '#'
                else:
                    temp[i][j] = '|'
            else:
                if lumberyards > 0 and trees > 0:
                    temp[i][j] = '#'
                else:
                    temp[i][j] = '.'
    return temp
    
def get_adjacent(coord, grid):
    row = coord[0]
    col = coord[1]
    trees = 0
    lumberyards = 0
    pos_list = []

    #left side
    if row > 0:
        pos_list.append((row - 1, col))
        if col > 0:
            pos_list.append((row - 1, col - 1))
        if col < len(grid[0]) - 1:
            pos_list.append((row - 1, col + 1))
    #right side
    if row < len(grid) - 1:
        pos_list.append((row + 1, col))
        if col > 0:
            pos_list.append((row + 1, col - 1))
        if col < len(grid[0]) - 1:
            pos_list.append((row + 1, col + 1))
    
    #top and bottom
    if col > 0:
        pos_list.append((row, col - 1))
    if col < len(grid[0]) - 1:
        pos_list.append((row, col + 1))

    for pos in pos_list:

        square = grid[pos[0]][pos[1]]
        if square == '#':
            lumberyards += 1
        elif square == '|':
            trees += 1
    return trees, lumberyards

def calc_score(grid):
    trees = 0
    lumberyards = 0
    for row in grid:
        for char in row:
            if char == '|':
                trees += 1
            elif char == '#':
                lumberyards += 1
    return trees * lumberyards

size = 50
grid = []
for i in range(size):
    grid.append([])
with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

for i, line in enumerate(lines):
    for char in line.strip():
        grid[i].append(char)

minute = 0
while minute < 1000000000:
    if minute % 100 == 0:
        print(f"minute: {minute} score: {calc_score(grid)}")
    grid = process(grid)
    minute += 1

print(calc_score(grid))