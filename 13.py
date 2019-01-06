import sys


def printMap(map, carts=[]):
    print(' ', end='')
    for x in range(len(map[0])):
        print((x % 10), end='')
    print()
    for y in range(len(map)):
        print((y % 10), end='')
        for x in range(len(map[y])):
            for cart in carts:
                if cart['x'] == x and cart['y'] == y:
                    print(cart['direction'], end='')
                    break
            else:
                print(map[y][x], end='')
        print()


def moveCart(cart):
    if cart['direction'] == '>':
        cart['x'] += 1
    elif cart['direction'] == '<':
        cart['x'] -= 1
    elif cart['direction'] == '^':
        cart['y'] -= 1
    elif cart['direction'] == 'v':
        cart['y'] += 1
    else:
        raise Exception('Unclear what happend')


def turnCart(cart, move):
    directions = ['^', '>', 'v', '<']
    current = directions.index(cart['direction'])
    if move == 'left':
        cart['direction'] = directions[current - 1]
    if move == 'right':
        cart['direction'] = directions[(current + 1) % 4]


def checkCollections(carts):
    cords = set()
    for cart in carts:
        if (cart['x'], cart['y']) in cords:
            raise Exception('Collision at %ix%i!' % (cart['x'], cart['y']))
        cords.add((cart['x'], cart['y']))

map = []
carts = []
y = 0
for row in sys.stdin.read().strip().split('\n'):
    new_row = []
    for x in range(len(row)):
        if row[x] in ['v', '^', '<', '>']:
            carts.append({'direction': row[x], 'x': x, 'y': y, 'states': ['left', 'straight', 'right']})
            if row[x] in ['v', '^']: new_row.append('|')
            if row[x] in ['<', '>']: new_row.append('-')
        else:
            new_row.append(row[x])
    map.append(new_row)
    y += 1

print('Initial map:')
printMap(map)
print('Carts:')
print(carts)
print('Initial map with carts:')
printMap(map, carts)

tick = 0
while True:
#    print('Tick: %i' % tick)
    for cart in sorted(carts, key=lambda k: (k['y'], k['x'])):
        if map[cart['y']][cart['x']] == '|':
            pass
        elif map[cart['y']][cart['x']] == '-':
            pass
        elif map[cart['y']][cart['x']] == '/':
            if cart['direction'] in ['^', 'v']:
                turnCart(cart, 'right')
            else:
                turnCart(cart, 'left')
        elif map[cart['y']][cart['x']] == '\\':
            if cart['direction'] in ['^', 'v']:
                turnCart(cart, 'left')
            else:
                turnCart(cart, 'right')
        elif map[cart['y']][cart['x']] == '+':
            move = cart['states'].pop(0)
            cart['states'].append(move)
            turnCart(cart, move)
        else:
            print(cart)
            print(x, y, map[cart['y']][cart['x']])
            raise Exception('What happend here?')
        moveCart(cart)
        checkCollections(carts)
        continue
#    printMap(map, carts)
    tick += 1
