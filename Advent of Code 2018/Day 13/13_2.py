import sys

class Cart():
    def __init__(self, id, pos, dir='u'):
        self.id = id
        self.pos = pos
        self.dir = dir
        self.intersection_count = 0
        self.deleted = False

    def print(self, end=1):
        if end == 0:
            print("ID: " + str(self.id) + " Pos: " + str(self.pos) + " Dir: " + str(self.dir), end='')
        else:
            print("ID: " + str(self.id) + " Pos: " + str(self.pos) + " Dir: " + str(self.dir))

    def move(self):
        if cart.dir == 'u':
            cart.move_up()
        elif cart.dir == 'd':
            cart.move_down()
        elif cart.dir == 'r':
            cart.move_right()
        elif cart.dir == 'l':
            cart.move_left()

    def move_up(self):
        self.pos = (self.pos[0], self.pos[1] - 1)
    
    def move_down(self):
        self.pos = (self.pos[0], self.pos[1] + 1)

    def move_left(self):
        self.pos = (self.pos[0] - 1, self.pos[1])

    def move_right(self):
        self.pos = (self.pos[0] + 1, self.pos[1])

    def turn_left(self):
        if cart.dir == 'u':
            cart.dir = 'l'
        elif cart.dir == 'l':
            cart.dir = 'd'
        elif cart.dir == 'd':
            cart.dir = 'r'
        elif cart.dir == 'r':
            cart.dir = 'u'     

    def turn_right(self):
        if cart.dir == 'u':
            cart.dir = 'r'
        elif cart.dir == 'l':
            cart.dir = 'u'
        elif cart.dir == 'd':
            cart.dir = 'l'
        elif cart.dir == 'r':
            cart.dir = 'd'

def fix_track(tracks, x, y):
    u = None if y == 0 else tracks[y-1][x]
    d = None if y == len(tracks) - 1 else tracks[y+1][x]
    l = None if x == 0 else tracks[y][x-1]
    r = None if x == len(tracks[y]) - 1 else tracks[y][x+1]
    if u == '|' and d == '|' and l == '-' and r == '-':
        tracks[y][x] = '+'
    elif (u == '|' and r == '-') or (d == '|' and l == '-'):
        tracks[y][x] = "\\"
    elif (u == '|' and l == '-') or (d == '|' and r == '-'):
        tracks[y][x] = "/"
    elif cart.dir in ['u', 'd']:
        tracks[y][x] = '|'
    else:
        tracks[y][x] = '-'

def move_cart(track, cart):
    if track == '|' or track == '-':
            cart.move()      
    elif track == '/':
        if cart.dir == 'r' or cart.dir == 'l':
            cart.turn_left()
        elif cart.dir == 'd' or cart.dir == 'u':
            cart.turn_right()
        cart.move()
    elif track == '\\':
        if cart.dir == 'l' or cart.dir == 'r':
            cart.turn_right()
        elif cart.dir == 'd' or cart.dir == 'u':
            cart.turn_left()
        cart.move() 
    elif track == '+':
        if cart.intersection_count == 0:
            cart.turn_left()
        elif cart.intersection_count == 2:
            cart.turn_right()
        cart.intersection_count += 1
        cart.intersection_count %= 3
        cart.move()

#process input
with open('input.txt', 'r') as inputFile:
    tracks = inputFile.readlines()

for i, track in enumerate(tracks):
    tracks[i] = list(track.strip('\n'))

#find cart locations and fix the spots in track where carts are
carts = []
cart_positions = set()
for y in range(len(tracks)):
    for x in range(len(tracks[y])):
        if tracks[y][x] in ['>', '<', 'v', '^']:
            cart = Cart(len(carts), (x, y))
            if tracks[y][x] == '>':
                cart.dir = 'r'
            elif tracks[y][x] == '<':
                cart.dir = 'l'
            elif tracks[y][x] == '^':
                cart.dir = 'u'
            elif tracks[y][x] == 'v':
                cart.dir = 'd'
            carts.append(cart)

            #fix track
            fix_track(tracks, x, y)

#need to sort carts by top to bottom left to right position
while True:
    if (len(carts) < 2):
        carts[0].print()
        sys.exit()

    #sort carts
    carts = sorted(carts, key=lambda cart: cart.pos[0])
    carts = sorted(carts, key=lambda cart: cart.pos[1])

    #advance carts
    i = 0
    while i < len(carts):
        cart = carts[i]
        if cart.deleted == False:
            cart_positions.discard(cart.pos)
            x = cart.pos[0]
            y = cart.pos[1]
            track = tracks[y][x]
            move_cart(track, cart)

            if cart.pos in cart_positions:
                cart_positions.discard(cart.pos)
                cart.deleted = True
                for j in range(len(carts)):
                    if carts[j].pos == cart.pos:
                        carts[j].deleted = True
            else:
                cart_positions.add(cart.pos)
        i += 1

    #remove deleted carts
    carts = [cart for cart in carts if cart.deleted == False]

