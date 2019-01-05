with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()
coord_counts = {}
for line in lines:
    line = line.split()
    #0:id 1:@ 2:x,y 3:wxh
    coord = line[2][:-1].split(',')
    dims = line[3].split('x')
    for i in range(int(coord[0]), int(coord[0]) + int(dims[0])):
        for j in range(int(coord[1]), int(coord[1]) +int(dims[1])):
            coord_counts[(i,j)] = coord_counts.get((i,j), 0) + 1

count = 0
for entry in coord_counts:
    if coord_counts[entry] > 1:
        count += 1

print(count)
