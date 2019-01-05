class Nanobot:
    def __init__(self, id, pos, range):
        self.id = id
        self.pos = pos
        self.range = range

    def in_range(self, target):
        distance = abs(self.pos[0] - target.pos[0]) + abs(self.pos[1] - target.pos[1]) + abs(self.pos[2] - target.pos[2])
        return distance <= self.range

    def print(self):
        print(f"ID: {self.id} POS: {self.pos} Range:{self.range}")

id_counter = 0
bots = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        parts = line.split('=')
        pos = parts[1].split('>')
        pos = pos[0].split(',')
        pos = (int(pos[0][1:]), int(pos[1]), int(pos[2]))
        range = int(parts[2].strip())
        bots.append(Nanobot(id_counter, pos, range))
        id_counter += 1

strongest_bot = max(bots, key=lambda bot: bot.range)
in_range_count = 0
for bot in bots:
    if strongest_bot.in_range(bot):
        in_range_count += 1

print(in_range_count)