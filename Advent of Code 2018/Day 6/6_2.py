points = []
max_x = 0
max_y = 0
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        parts = line.split(',')
        x = int(parts[0].strip())
        y = int(parts[1].strip())
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        points.append((x, y))

region_sum = 0
for i in range(max_x + 1):
    for j in range(max_y + 1):
        man_sum = 0
        for point in points:
            dist = abs(point[0] - i) + abs(point[1] - j)
            man_sum += dist
        if man_sum < 10000:
            region_sum += 1

print(region_sum)