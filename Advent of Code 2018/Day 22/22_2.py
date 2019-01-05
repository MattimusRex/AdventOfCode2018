import queue
import sys

class Cave:
    def __init__(self, depth, target, start, extra):
        self.depth = depth
        self.target = target
        self.start = start
        self.extra = extra
        self.risk_level = 0
        self.cave = []

    def fill_geo_indexes(self, geo_index):
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
                if (x, y) == self.target:
                    geo_index[y][x] = 0
                else:
                    erosion1 = self.get_erosion_level(x-1, y, geo_index)
                    erosion2 = self.get_erosion_level(x, y-1, geo_index)
                    geo_index[y][x] = erosion1 * erosion2


    def get_geo_index(self, col, row, geo_index):
        return geo_index[row][col]

    def get_erosion_level(self, col, row, geo_index):
        index = self.get_geo_index(col, row, geo_index)
        return (index + DEPTH) % 20183

    def get_type(self, col, row, geo_index):
        erosion_level = self.get_erosion_level(col, row, geo_index)
        if erosion_level % 3 == 0:
            return '.'
        elif erosion_level % 3 == 1:
            return '='
        else:
            return '|'

    def map_cave(self):
        x_border = self.target[0] + self.extra
        y_border = self.target[1] + self.extra

        geo_index = []
        for y in range(y_border):
            self.cave.append([0] * x_border)
            geo_index.append([-1] * x_border)

        self.fill_geo_indexes(geo_index)
        for y, row in enumerate(self.cave):
            for x, col in enumerate(row):
                if self.cave[y][x] == 0:
                    t = self.get_type(x, y, geo_index)
                    self.cave[y][x] = t
                    if y <= self.target[1] and x <= self.target[0]:
                        if t == '=':
                            self.risk_level += 1
                        elif t == '|':
                            self.risk_level += 2
    
    def print(self):
        for y, row in enumerate(self.cave):
            for x, c in enumerate(row):
                if (x, y) == self.target:
                    print('T', end='')
                else:
                    print(c, end='')
            print()


class Node:
    def __init__(self, pos, dist, time, tool, path):
        self.pos = pos
        self.dist = dist
        self.time = time
        self.tool = tool
        self.score = dist + time
        self.path = path
        self.path.append(self)

    def get_adj_pos(self, target, extra):
        row = self.pos[1]
        col = self.pos[0]
        adj = []
        if col > 0:
            adj.append((col - 1, row))
        if col < target[0] - 1 + extra:
            adj.append((col + 1, row))
        if row > 0:
            adj.append((col, row - 1))
        if row < target[1] - 1 + extra:
            adj.append((col, row + 1))
        
        return adj
    
    def get_id(self):
        return (self.pos, self.tool)

    def __lt__(self, other):
        return self.score < other.score

    def print(self, path):
        print(f"Time: {self.time} Tool: {self.tool}")
        if path:
            for p in self.path:
                print(f"Time: {p.time} Tool: {p.tool} Pos: {p.pos}")
    

def get_distance(pos, target):
    return abs(target[0] - pos[0]) + abs(target[1] - pos[1])

#col, row aka x, y
#TEST DATA

# DEPTH = 510
# TARGET = (10, 10)
# START = (0, 0)


#between 1071, 1096 not 1080
DEPTH = 4080
TARGET = (14, 785)
START = (0, 0)


EXTRA = 50

cave = Cave(DEPTH, TARGET, START, EXTRA)
cave.map_cave()
print(cave.risk_level)

node = Node(START, get_distance(START, TARGET), 0, 'T', [])
nodes = queue.PriorityQueue()
nodes.put(node)
visited = set()

while True:
    try:
        node = nodes.get(False)
    except queue.Empty:
        sys.exit("shit broke")
    else:
        if node.get_id() not in visited:
            if node.pos == TARGET:
                if node.tool == 'C':
                    node.time += 7
                node.print(False)
                continue
            visited.add(node.get_id())
            #get adjacent squares
            adj = node.get_adj_pos(cave.target, EXTRA)

            #add adjacent squares if possible
            for pos in adj:
                new_nodes = []
                if cave.cave[pos[1]][pos[0]] == '.':
                    if node.tool == 'N':
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 8, 'T', [x for x in node.path]))
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 8, 'C', [x for x in node.path]))
                    else:
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 1, node.tool, [x for x in node.path]))
                elif cave.cave[pos[1]][pos[0]] == '=':
                    if node.tool == 'T':
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 8, 'N', [x for x in node.path]))
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 8, 'C', [x for x in node.path]))
                    else:
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 1, node.tool, [x for x in node.path]))
                elif cave.cave[pos[1]][pos[0]] == '|':
                    if node.tool == 'C':
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 8, 'T', [x for x in node.path]))
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 8, 'N', [x for x in node.path]))
                    else:
                        new_nodes.append(Node(pos, get_distance(pos, TARGET), node.time + 1, node.tool, [x for x in node.path]))
                for n in new_nodes:
                            if n.get_id not in visited:
                                nodes.put(n)






