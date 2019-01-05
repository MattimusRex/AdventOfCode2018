class Node:
    def __init__(self, num_children, num_meta):
        self.num_children = int(num_children)
        self.num_meta = int(num_meta)
        self.children = []
        self.meta = []

    def get_value(self):
        #num children gets messed up when creating data structure, don't use it
        if len(self.children) == 0:
            return sum(self.meta)
        value = 0
        for index in self.meta:
            #meta is 1 indexed but stored in Node object as 0 index
            index -= 1
            if index < len(self.children):
                value += self.children[index].get_value()
        return value

with open('input.txt', 'r') as inputFile:
    data = inputFile.read().split()

nodes = []
i = 2
nodes.append(Node(data[0], data[1]))
while len(nodes) > 0:
    node = nodes.pop()
    if node.num_children > 0:
        node.num_children -= 1
        new_node = Node(data[i], data[i+1])
        node.children.append(new_node)
        nodes.append(node)
        nodes.append(new_node)
        i += 2
    else:
        j = 0
        while j < node.num_meta:
            node.meta.append(int(data[i]))
            i += 1
            j += 1

print(node.get_value())