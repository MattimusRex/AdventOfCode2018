class Worker:
    def __init__(self, id):
        self.id = id
        self.time_left = self.get_time_left(id)

    def get_time_left(self, id):
        return (ord(id) - 64) + 60

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
seconds = 0
workers = [None] * 5
while len(nodes_to_process) > 0 or len(nodes) > 0:
    #get nodes to workers
    for i, worker in enumerate(workers):
        if worker is None:
            temp_node = get_next_node(nodes_to_process)
            if temp_node is not None:
                workers[i] = Worker(temp_node.id)
                nodes_to_process.remove(temp_node)
    
    #get lowest time left of workers
    min_time = 10000000
    for worker in workers:
        if worker is not None:
            min_time = min(min_time, worker.time_left)
    
    #remove this amount of time from all workers
    seconds += min_time
    for i, worker in enumerate(workers):
        if worker is not None:
            worker.time_left -= min_time
            #if worker is finished, process node
            if worker.time_left == 0:
                answer += worker.id
                node = nodes[worker.id]
                for edge in node.edges:
                    nodes[edge].prereqs.remove(node.id)
                    if not nodes[edge].has_prereqs():
                        nodes_to_process.append(nodes[edge])
                nodes.pop(node.id)
                workers[i] = None

print(seconds)

