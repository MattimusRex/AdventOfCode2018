GRID_SERIAL_NUMBER = 9005

def calc_power(pos):
    rackID = pos[0] + 10
    power = rackID * pos[1]
    power += GRID_SERIAL_NUMBER
    power *= rackID
    power = (power // 100) % 10
    power -= 5
    return power

def calc_power_grid(grid):
    for y in range(1, len(grid)):
        for x in range(1, len(grid)):
            grid[y][x] = calc_power((x, y))

def calc_power_square(pos, size, grid):
    power = 0
    for y in range(pos[1], pos[1] + size):
        for x in range(pos[0], pos[0] + size):
            power += grid[y][x]
    return power

def calc_power_size(size, grid):
    max_power = 0
    power = 0
    for y in range(1, 1 + size):
        for x in range(1, 1 + size):
            power += grid[y][x]
    initial_power = power
    max_power = power
    max_pos = (1,1)

    for y in range(1, 300 - size + 1):
        for x in range(2, 300 - size + 1):
            for i in range(y, y + size):
                power -= grid[i][x - 1]
                power += grid[i][x + size - 1]
            if power > max_power:
                max_power = power
                max_pos = (x, y)
        for i in range(1, 1 + size):
            initial_power -= grid[y][i]
            initial_power += grid[y + size][i]
        power = initial_power
        if power > max_power:
            max_power = power
            max_pos = (x, y)
    return (max_power, max_pos)


grid = []
for i in range(301):
    row = [0] * 301
    grid.append(row)

calc_power_grid(grid)

max_power = 0
for size in range(1, 301):
    print(size)
    power_pos = calc_power_size(size, grid)
    if power_pos[0] > max_power:
        max_power = power_pos[0]
        max_pos = (power_pos[1][0], power_pos[1][1], size)

print(max_pos)
print(max_power)