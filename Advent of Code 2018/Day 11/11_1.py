GRID_SERIAL_NUMBER = 9005

def calc_power(pos):
    rackID = pos[0] + 10
    power = rackID * pos[1]
    power += GRID_SERIAL_NUMBER
    power *= rackID
    power = (power // 100) % 10
    power -= 5
    return power


def calc_power_grid(pos):
    power_sum = 0
    for y in range(pos[1], pos[1] + 3): 
        for x in range(pos[0], pos[0] + 3):
            power_sum += calc_power((x, y))
    return power_sum
        
max_power = 0
for y in range(1, 299):
    for x in range(1, 299):
        power = calc_power_grid((x, y))
        if power > max_power:
            max_power = power
            max_pos = (x, y)

print(max_pos)
print(max_power)