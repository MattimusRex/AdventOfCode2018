class Nanobot:
    def __init__(self, id, pos, radius):
        self.id = id
        self.pos = pos
        self.radius = radius

    def in_range(self, pos):
        distance = abs(self.pos[0] - pos[0]) + abs(self.pos[1] - pos[1]) + abs(self.pos[2] - pos[2])
        return distance <= self.radius

    def print(self):
        print(f"ID: {self.id} POS: {self.pos} Radius:{self.radius}")


def m_dist(pos):
    return abs(pos[0]) + abs(pos[1]) + abs(pos[2])

id_counter = 0
bots = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        parts = line.split('=')
        pos = parts[1].split('>')
        pos = pos[0].split(',')
        pos = (int(pos[0][1:]), int(pos[1]), int(pos[2]))
        radius = int(parts[2].strip())
        bots.append(Nanobot(id_counter, pos, radius))
        id_counter += 1

# x_min = bots[0].pos[0] - bots[0].radius
# x_max = bots[0].pos[0] + bots[0].radius
# y_min = bots[0].pos[1] - bots[0].radius
# y_max = bots[0].pos[1] + bots[0].radius
# z_min = bots[0].pos[2] - bots[0].radius
# z_max = bots[0].pos[2] + bots[0].radius

# for bot in bots:
#     x_min = min(x_min, bot.pos[0] - bot.radius)
#     x_max = max(x_max, bot.pos[0] + bot.radius)
#     y_min = min(y_min, bot.pos[1] - bot.radius)
#     y_max = max(y_max, bot.pos[1] + bot.radius)
#     z_min = min(z_min, bot.pos[2] - bot.radius)
#     z_max = max(z_max, bot.pos[2] + bot.radius)

#809
#118900350
#111615413

x_min = 51119471 - 10
x_max = 51119471 + 10
y_min = 15076957 - 10
y_max = 15076957 + 10
z_min = 45418985 - 10
z_max = 45418985 + 10
step = 1

best_pos = None
max_count = -1
for x in range(x_min, x_max + 1, step):
    for y in range(y_min, y_max + 1, step):
        for z in range(z_min, z_max  +1, step):
            pos = (x, y, z)
            count = 0
            for bot in bots:
                if bot.in_range(pos):
                    count += 1
                if count > max_count:
                    max_count = count
                    best_pos = pos
                elif count == max_count:
                    if m_dist(pos) < m_dist(best_pos):
                        best_pos = pos

print(f"Best Position: {best_pos} in range of {max_count} bots")
print(m_dist(best_pos))

# pos = (51119516, 15197526, 45539508)
# in_range = 810
# while in_range >= 810:
#     pos = (pos[0], pos[1] - 1000, pos[2] - 1000)
#     count = 0
#     for bot in bots:
#         if bot.in_range(pos):
#             count += 1
#     in_range = count

# print(pos)
# print(m_dist(pos))




# min_distance = 10000000
# for candidate in candidates:
#     distance = abs(candidate[0] - 0) + abs(candidate[1] - 0) + abs(candidate[2] - 0)
#     min_distance = min(min_distance, distance)

# print(min_distance)
            




#checked = set()
# max_count = 0
# candidates = []
# bots = sorted(bots, key=lambda bot: bot.radius)
# for i in range(len(bots)):
#     if max_count > len(bots) - i:
#         break
#     bot = bots[i]
#     bot.print()
#     x_min = bot.pos[0] - bot.radius
#     x_max = bot.pos[0] + bot.radius
#     y_min = bot.pos[1] - bot.radius
#     y_max = bot.pos[1] + bot.radius
#     z_min = bot.pos[2] - bot.radius
#     z_max = bot.pos[2] + bot.radius
#     for x in range(x_min, x_max + 1):
#         for y in range(y_min, y_max + 1):
#             for z in range(z_min, z_max + 1):
#                 pos = (x, y, z)
#                 if pos not in checked:
#                     checked.add(pos)
#                     count = 1
#                     for j in range(i + 1, len(bots)):
#                         target = bots[j]
#                         if target.in_range(pos):
#                             count += 1
#                     if count > max_count:
#                         max_count = count
#                         candidates = []
#                         candidates.append(pos)
#                     elif count == max_count:
#                         candidates.append(pos)#