class Node:
    def __init__(self, id, pos, vel):
        self.id = id
        self.pos = pos
        self.vel = vel

    def advance(self):
        x = self.pos[0] + self.vel[0]
        y = self.pos[1] + self.vel[1]
        self.pos = (x, y)

    def get_distance(self, node):
        x_dist = node.pos[0] - self.pos[0]
        y_dist = node.pos[1] - self.pos[1]
        return (x_dist * x_dist) + (y_dist * y_dist)

def print_grid(nodes, positions, node, other_node):
    min_x = min(node.pos[0], other_node.pos[0])
    max_x = max(node.pos[0], other_node.pos[0])
    min_y = min(node.pos[1], other_node.pos[1])
    max_y = max((node.pos[1], other_node.pos[1]))
    min_x -= 50
    max_x += 50
    min_y -= 50
    max_y += 50   
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if (j, i) in positions:
                print("#", end='')
            else:
                print(".", end='')
        print()
    print()


def calc_longest_distance(nodes):
    max_dist = 0
    for node in nodes:
        for other_node in nodes:
            dist = node.get_distance(other_node)
            if dist > max_dist:
                max_dist = dist
                node1 = node
                node2 = other_node
    return (max_dist, node1, node2)


#process input into nodes
nodes = []
positions = set()
id_counter = 1
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        pos = line[line.find("<") + 1:line.find(">")]
        pos = pos.split(",")
        pos = (int(pos[0].strip()), int(pos[1].strip()))

        line = line[line.find(">") + 1:]
        vel = line[line.find("<") + 1:line.find(">")]
        vel = vel.split(",")
        vel = (int(vel[0].strip()), int(vel[1].strip()))
        positions.add(pos)
        node = Node(id_counter, pos, vel)
        nodes.append(node)

dist, node1, node2 = calc_longest_distance(nodes)
seconds = 0
while seconds < 100000:
    #print(seconds)
    dist = node1.get_distance(node2)
    # if seconds % 100 == 0:
    #     print(dist)
    if dist < 15000:
        print(seconds)
        print_grid(nodes, positions, node1, node2)
    positions.clear()
    for node in nodes:
        node.advance()
        positions.add(node.pos)
    seconds += 1
