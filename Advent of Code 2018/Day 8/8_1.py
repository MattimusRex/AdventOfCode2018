class Node:
    def __init__(self, num_children, num_meta):
        self.num_children = int(num_children)
        self.num_meta = int(num_meta)

with open('input.txt', 'r') as inputFile:
    data = inputFile.read().split()

nodes = []
meta_sum = 0
i = 2
nodes.append(Node(data[0], data[1]))
while len(nodes) > 0:
    node = nodes.pop()
    if node.num_children > 0:
        node.num_children -= 1
        nodes.append(node)
        new_node = Node(data[i], data[i+1])
        nodes.append(new_node)
        i += 2
    else:
        j = 0
        while j < node.num_meta:
            meta_sum += int(data[i])
            i += 1
            j += 1

print(meta_sum)