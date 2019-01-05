class stream:
    def __init__(self, start):
        self.start = start
        self.current = start

    def fill(self, clay, r_water, s_water):
        while (self.current != self.start):
            self.spread(clay, r_water, s_water)
            self.current = (self.current[0] - 1, self.current[1])
        self.spread(clay, r_water, s_water)

    def find_next_bottom(self, clay, r_water, s_water):
        down = (self.current[0] + 1, self.current[1])
        while down not in clay and down not in r_water and down not in s_water:
            if down[0] == max_y + 1:
                return False
            self.current = down
            r_water.add(self.current)
            down = (self.current[0] + 1, self.current[1])
        return True

    def spread(self, clay, r_water, s_water):
        head = self.current
        clay_left = True
        clay_right = True
        running = False
        
        down = (self.current[0] + 1, self.current[1])
        if down in r_water:
            return

        #get left border
        left = (self.current[0], self.current[1] - 1)
        while left not in clay:
            self.current = left
            down = (self.current[0] + 1, self.current[1])
            if down not in clay and down not in s_water:
                new_stream = stream(self.current)
                new_stream.solve(clay, r_water, s_water)
                running = True
                clay_left = False
                break
            left = (self.current[0], self.current[1] - 1)

        #get right border
        self.current = head

        right = (self.current[0], self.current[1] + 1)
        while right not in clay:
            self.current = right
            down = (self.current[0] + 1, self.current[1])
            if down not in clay and down not in s_water:
                new_stream = stream(self.current)
                new_stream.solve(clay, r_water, s_water)
                running = True
                clay_right = False
                break
            right = (self.current[0], self.current[1] + 1)
        
        if clay_left:
            left = (left[0], left[1] + 1)
        if clay_right:
            right = (right[0], right[1] - 1)

        if running:
            for i in range(left[1], right[1] + 1):
                if (self.current[0], i) not in s_water:
                    r_water.add((self.current[0], i))
        else:
            for i in range(left[1], right[1] + 1):
                s_water.add((self.current[0], i))
                r_water.discard((self.current[0], i))

        self.current = head
        
    def solve(self, clay, r_water, s_water):
        found_bottom = self.find_next_bottom(clay, r_water, s_water)
        if not found_bottom:
            return len(r_water) + len(s_water)
        else:
            self.fill(clay, r_water, s_water)
        return len(r_water) + len(s_water)


def print_map(clay, r_water, s_water, min_y, max_y, min_x, max_x):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (y, x) in s_water:
                print('~', end='')
            elif (y, x) in r_water:
                print('|', end='')
            # elif (y, x) in s_water:
            #     print('~', end='')
            elif (y, x) in clay:
                print('#', end='')
            else:
                print('.',end='')
        print()

def process_input(line, clay):
    parts = line.strip().split(',')
    first_part = parts[0].split('=')
    if first_part[0] == 'x':
        x = int(first_part[1])
    else:
        y = int(first_part[1])

    second_part = parts[1].strip().split('=')
    var = second_part[0]
    second_part = second_part[1].split('..')
    start = int(second_part[0])
    stop = int(second_part[1])

    #row, col
    for i in range(start, stop + 1):
        if var == 'x':
            clay.add((y, i))
        else:
            clay.add((i, x))

clay = set()
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        process_input(line, clay)

min_y = 10000000000
max_y = 0
min_x = 100000000
max_x = 0

for pos in clay:
    min_y = min(pos[0], min_y)
    max_y = max(pos[0], max_y)
    min_x = min(min_x, pos[1])
    max_x = max(max_x, pos[1])



r_water = set()
s_water = set()
start_stream = stream((4, 500))

start_stream.solve(clay, r_water, s_water)

#print_map(clay, r_water, s_water, min_y - 10, max_y + 10, min_x - 10, max_x + 10)
print(len(s_water))
s_water.discard(r_water)
print(len(s_water))




    





