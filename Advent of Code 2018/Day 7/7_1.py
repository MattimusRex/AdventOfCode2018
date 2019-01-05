class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.prereqs = set()
    
    def has_prereqs(self):
        return len(self.prereqs) > 0

#returns the node with the lowest alphabetical id
def get_next_node(nodes):
    min_node = None
    for node in nodes:
        if min_node is None or node.id < min_node.id:
            min_node = node
    return min_node

nodes = {}
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        #1 is prereq node, 7 is edge node
        parts = line.split()
        
        #ensure both nodes are in dict
        if parts[1] not in nodes:
            nodes[parts[1]] = Node(parts[1])
        if parts[7] not in nodes:
            nodes[parts[7]] = Node(parts[7])
        
        nodes[parts[1]].edges.append(parts[7])
        nodes[parts[7]].prereqs.add(parts[1])

#this would be faster with a priority queue
nodes_to_process = []
for key, value in nodes.items():
    if not value.has_prereqs():
        nodes_to_process.append(value)

#get lowest alphabet node without prereqs and remove it from its following nodes
answer = ''
while len(nodes_to_process) > 0:
    node = get_next_node(nodes_to_process)
    nodes_to_process.remove(node)
    answer += node.id
    for edge in node.edges:
        nodes[edge].prereqs.remove(node.id)
        if not nodes[edge].has_prereqs():
            nodes_to_process.append(nodes[edge])

print(answer)

