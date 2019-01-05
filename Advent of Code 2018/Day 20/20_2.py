import sys
import queue

class Node:
    def __init__(self, index, dir, distance):
        self.index = index
        self.distance = distance
        self.dir = dir

def create_node(index, dir, node):
    if index in visited:
        print(f"{index} {string[index-5:index+5]}")
        temp = None
    elif opposites[dir] == node.dir:
        temp = None
    else:
        temp = Node(index, dir, node.distance + 1)
    return temp


with open('input.txt', 'r') as inputFile:
    string = inputFile.readline()

#string = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'

opposites = {'N':'S', 'S':'N', 'W':'E', 'E':'W'}

char_count = 11160

node = Node(1, string[1], 1)
to_do = [node]
visited = set()
answer = 0
count = {}
while len(to_do) > 0:
    node = to_do.pop()
    if node is None:
        continue
    if node.index in visited:
        print(node.index)
        continue
    visited.add(node.index)
    if node.distance >= 1000:
        count[node.index] = count.get(node.index, 0) + 1
        answer += 1
    i = node.index
    if string[i + 1].isalpha():
        temp = create_node(i + 1, string[i + 1], node)
        to_do.append(temp)
    elif string[i + 1] == '(':
        para_count = 1
        j = i + 2
        temp = create_node(j, string[j], node)
        to_do.append(temp)
        while para_count > 0:
            if string[j] == '(':
                para_count += 1
            elif string[j] == ')':
                para_count -= 1
            elif string[j] == '|' and para_count == 1:
                if string[j + 1] == ')':
                    k = j + 1
                    while not string[k].isalpha():
                        if string[k] == '|':
                            break
                        k += 1
                    if string[k].isalpha():
                        temp = create_node(k, string[k], node)
                        to_do.append(temp)
                else:
                    temp = create_node(j + 1, string[j + 1], node)
                    to_do.append(temp)
            j += 1
    elif string[i + 1] == '|' or string[i + 1] == ')':
        continue

for k,v in count.items():
    if v > 2:
        print(f"{k} {v}")
print(answer)




