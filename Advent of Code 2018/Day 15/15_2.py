import sys

#npc: list of npcs
#returns: sorted list of npcs in reading order (left to right, top to bottom)
def reading_order_sort_npcs(npcs):
    npcs = sorted(npcs, key=lambda npc: npc.pos[1])
    npcs = sorted(npcs, key=lambda npc: npc.pos[0])
    return npcs

def reading_order_sort_positions(positions):
    positions = sorted(positions, key=lambda pos: pos[1])
    positions = sorted(positions, key=lambda pos: pos[0])
    return positions

#pos: a position in (row, col) form
#returns: a set of the adjacent positions out of the possible 4 (u, d, l, r)
def get_adjacent_spaces(pos):
    adj_spaces = set()
    row = pos[0]
    col = pos[1]
    if row > 1:
        adj_spaces.add((row - 1, col))
    if row < len(state.game_map) - 1:
        adj_spaces.add((row + 1, col))
    if col > 1:
        adj_spaces.add((row, col - 1))
    if col < len(state.game_map[0]) - 1:
        adj_spaces.add((row, col + 1))
    return adj_spaces

class Game_State:
    def __init__(self, game_map, pow):
        self.rounds_completed = 0
        self.current_positions = []
        self.elves = {}
        self.goblins = {}
        self.turn_order = []
        self.game_map = game_map
        
        id_counter = 0
        for y, row in enumerate(self.game_map):
            for x, col in enumerate(row):
                if col == 'E':
                    elf = NPC(id_counter, 'elf', y, x, (y, x), pow)
                    self.elves[elf.id] = elf
                elif col == 'G':
                    goblin = NPC(id_counter, 'goblin', y, x, (y, x), pow)
                    self.goblins[goblin.id] = goblin
                id_counter += 1

    def game_over(self):
        print("Game over man, game over!")

        hp_sum = 0
        for k, v in self.elves.items():
            hp_sum += v.hp
        for k, v in self.goblins.items():
            hp_sum += v.hp

        print(f"HP sum: {hp_sum}, Rounds: {state.rounds_completed}, Total: {hp_sum * state.rounds_completed}")
        sys.exit()

    #returns: list of the npcs in reading order
    def get_turn_order(self):
        self.turn_order = []
        for k, v in self.elves.items():
            self.turn_order.append(v)
        for k, v in self.goblins.items():
            self.turn_order.append(v)

        self.turn_order = reading_order_sort_npcs(self.turn_order)

    def is_empty(self, pos):
        return self.game_map[pos[0]][pos[1]] == '.'

    def print_game_map(self):
        for row in self.game_map:
            print(''.join(row))
                    
class NPC:
    def __init__(self, id, type, row, col, pos, pow):
        self.id = id
        self.type = type
        self.row = row
        self.col = col
        self.pos = (row, col)
        self.hp = 200
        self.atk_pwr = 3 if type == 'goblin' else pow
        self.dead = False

    def attack(self, target, state):
        target.take_damage(self.atk_pwr, state)

    def attack_first_target(self, targets, state):
        target = self.get_first_target(targets, state)
        if target is None:
            return False
        else:
            self.attack(target, state)
            return True

    def dies(self, state):
        if self.type == 'elf':
            state.elves.pop(self.id)
            print("Elf Dies")
            sys.exit()
        else:
            state.goblins.pop(self.id)
        self.dead = True
        state.game_map[self.row][self.col] = '.'

    #end: the position we are moving to
    #state: the game state
    #returns: the position adjacent to the npc that is on the shortest path to end
    def get_best_adj_pos(self, end, state):
        adj_positions = get_adjacent_spaces(self.pos)
        adj_positions = [pos for pos in adj_positions if state.is_empty(pos)]
        min_distance = 1000
        min_pos = []
        for start in adj_positions:
            if start == end:
                return start
            nodes = [start]
            visited = set()
            distance = 1
            next_level = []
            while len(nodes) > 0:
                node = nodes.pop()
                if node not in visited:
                    visited.add(node)
                    adj_spaces = get_adjacent_spaces(node)
                    for space in adj_spaces:
                        if state.is_empty(space) and space not in visited:
                            if space == end:
                                if distance < min_distance:
                                    min_distance = distance
                                    min_pos = [start]
                                elif distance == min_distance:
                                    min_pos.append(start)
                                break
                            else:
                                next_level.append(space)
                if len(nodes) == 0:
                    nodes = next_level
                    next_level = []
                    distance += 1
        
        if len(min_pos) == 0:
            return None
        else: 
            return reading_order_sort_positions(min_pos)[0]

    #positions: list of positions
    #state: game state
    #uses breadth first search to find reachable positions
    #returns the nearest position
    def get_chosen_position(self, positions, state):
        nearest_positions = set()
        positions = set(positions)
        nodes = []
        visited = set()
        nodes.append(self.pos)
        next_level = []
        level_counter = 0
        finish = False
        while len(nodes) > 0:
            node = nodes.pop()
            if node not in visited:
                visited.add(node)
                adj_spaces = get_adjacent_spaces(node)
                for space in adj_spaces:
                    if state.is_empty(space) and space not in visited:
                        if space in positions:
                            finish = True
                            nearest_positions.add(space)
                        next_level.append(space)
            if len(nodes) == 0:
                if not finish:
                    nodes = next_level
                    next_level = []
                    level_counter += 1
                else:
                    return reading_order_sort_positions(list(nearest_positions))[0]

        return None

    #targets: list of target npcs
    #state: the game state
    #returns: the first adjacent target according to reading order
    def get_first_target(self, targets, state):
        adj_spaces = get_adjacent_spaces(self.pos)

        adj_targets = []
        for target in targets:
            if target.pos in adj_spaces:
                adj_targets.append(target)
        
        min_hp = 10000
        for target in adj_targets:
            min_hp = min(min_hp, target.hp)

        adj_targets = [x for x in adj_targets if x.hp == min_hp]

        if len(adj_targets) == 0:
            return None
        else:
            return reading_order_sort_npcs(adj_targets)[0]

    #targets: list of targets:
    #state: game state
    #returns: list of positions adjacent to targets
    def get_in_range_positions(self, targets, state):
        in_range_positions = set()
        for target in targets:
            adj_spaces = get_adjacent_spaces((target.row, target.col))
            for space in adj_spaces:
                in_range_positions.add(space)
        
        in_range_positions = [pos for pos in in_range_positions if state.is_empty(pos)]
        return in_range_positions

    def identify_targets(self, state):
        if self.type == 'elf':
            return state.goblins.values()
        else:
            return state.elves.values()

    def move(self, pos, state):
        state.game_map[self.row][self.col] = '.'
        self.pos = pos
        self.row = pos[0]
        self.col = pos[1]
        if self.type == 'elf':
            state.game_map[self.row][self.col] = 'E'
        else:
            state.game_map[self.row][self.col] = 'G'

    def take_damage(self, damage, state):
        self.hp -= damage
        if self.hp <= 0:
            self.dies(state)


################################################
### game start ###
################################################
game_map = []
with open('input.txt', 'r') as inputFile:
    for line in inputFile.readlines():
        row = []
        for char in line.strip():
            row.append(char)
        game_map.append(row)

pow = 40
state = Game_State(game_map, pow)
while state.rounds_completed < 100:
    state.get_turn_order()
    for npc in state.turn_order:
        if npc.dead:
            continue
        targets = npc.identify_targets(state)
        if len(targets) == 0:
            state.game_over()

        #check if npc is adjacent to a target
        made_attack = npc.attack_first_target(targets, state) 
        if not made_attack:
            #get in range squares
            in_range_positions = npc.get_in_range_positions(targets, state)
            if len(in_range_positions) > 0:
                
                #narrow in range to chosen
                chosen_position = npc.get_chosen_position(in_range_positions, state)
                if chosen_position is not None:

                    #calculate distance from empty adj squares to chosen
                    step_pos = npc.get_best_adj_pos(chosen_position, state)
                    if step_pos is not None:
                        #step to closest adj square
                        npc.move(step_pos, state)

                        #attack if enemy in range
                        npc.attack_first_target(targets, state)

    state.rounds_completed += 1