class Node:
    def __init__(self, id, next=None, prev=None):
        self.id = id
        self.next = next
        self.prev = prev

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def print(self):
        node = self
        print(str(self.id) + ' ', end='')
        self = self.next
        while self != node:
            print(str(self.id) + ' ', end='')
            self = self.next
        print()

NUMBER_OF_PLAYERS = 416
LAST_MARBLE = 7161700

current_player = 1
scores = [0] * (NUMBER_OF_PLAYERS + 1)
current = Node(0)
current.prev = current
current.next = current
head = current

for i in range(1, LAST_MARBLE + 1):
    if i % 23 == 0:
        scores[current_player] += i
        for j in range(7):
            current = current.prev
        scores[current_player] += current.id
        current.delete()
        current = current.next
    else:
        current = current.next
        temp = Node(i, current.next, current)
        current.next = temp
        temp.next.prev = temp
        current = current.next

    if current_player == NUMBER_OF_PLAYERS:
        current_player = 1
    else:
        current_player += 1

print(max(scores))
