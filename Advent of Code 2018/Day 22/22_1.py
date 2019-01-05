def fill_geo_indexes(geo_index):
    geo_index[0][0] = 0
    #do all y = 0
    for x in range(1, len(geo_index[0])):
        geo_index[0][x] = x * 16807
    #do all x = 0
    for y in range(1, len(geo_index)):
        geo_index[y][0] = y * 48271

    #now fill in by row
    for y in range(1, len(geo_index)):
        for x in range(1, len(geo_index[0])):
            erosion1 = get_erosion_level(x-1, y, geo_index)
            erosion2 = get_erosion_level(x, y-1, geo_index)
            geo_index[y][x] = erosion1 * erosion2

    geo_index[TARGET[1]][TARGET[0]] = 0

def get_geo_index(col, row, geo_index):
    return geo_index[row][col]

def get_erosion_level(col, row, geo_index):
    index = get_geo_index(col, row, geo_index)
    return (index + DEPTH) % 20183

def get_type(col, row, geo_index):
    erosion_level = get_erosion_level(col, row, geo_index)
    if erosion_level % 3 == 0:
        return '.'
    elif erosion_level % 3 == 1:
        return '='
    else:
        return '|'

#TEST DATA
# DEPTH = 510
# TARGET = (10, 10)
# START = (0, 0)


DEPTH = 4080
#col, row aka x, y
TARGET = (14, 785)
START = (0, 0)

x_border = TARGET[0] + 1
y_border = TARGET[1] + 1

cave = []
geo_index = []
for y in range(y_border):
    cave.append([0] * x_border)
    geo_index.append([-1] * x_border)

fill_geo_indexes(geo_index)
print("done filling")

risk_level = 0
for y, row in enumerate(cave):
    for x, col in enumerate(row):
        if cave[y][x] == 0:
            t = get_type(x, y, geo_index)
            cave[y][x] = t
            if t == '=':
                risk_level += 1
            elif t == '|':
                risk_level += 2

print(risk_level)



