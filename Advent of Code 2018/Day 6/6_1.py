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

#points_count (point:count) is the number of coordinates closest to a particular point
#coordinates_point (coordinate:point) is the point nearest a particular coordinate
points_count = {}
coordinates_point = {}
for i in range(max_x + 1):
    for j in range(max_y + 1):
        min_dist = 1000000000
        tie = False
        for point in points:
            dist = abs(point[0] - i) + abs(point[1] - j)
            if dist == min_dist:
                tie = True
            elif dist < min_dist:
                min_dist = dist
                min_point = point
                tie = False
        if not tie:
            points_count[min_point] = points_count.get(min_point, 0) + 1
            coordinates_point[(i, j)] = min_point

#find all points that have coordinates on the edges because this indicates
#that this point's area stretches into infinity and should not be considered
edge_points = set()
for y in range(max_y + 1):
    if (0, y) in coordinates_point:
        edge_points.add(coordinates_point[(0, y)])
    if (max_x, y) in coordinates_point:
        edge_points.add(coordinates_point[(max_x, y)])

for x in range(max_x + 1):
    if (x, 0) in coordinates_point:
        edge_points.add(coordinates_point[(x, 0)])
    if (x, max_y) in coordinates_point:
        edge_points.add(coordinates_point[(x, max_y)])

max_area = 0
for point in points_count:
    if point not in edge_points and points_count[point] > max_area:
        max_area = points_count[point]

print(max_area)