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
                    if cart['collided']:
                        print('X', end='')
                    else:
                        print(cart['direction'], end='')
                    break
            else:
                print(map[y][x], end='')
        print()
    return


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
    return


def turnCart(cart, move):
    directions = ['^', '>', 'v', '<']
    current = directions.index(cart['direction'])
    if move == 'left':
        cart['direction'] = directions[current - 1]
    if move == 'right':
        cart['direction'] = directions[(current + 1) % 4]
    return


def checkCollections(carts):
    cords = set()
    collision_cords = []
    for cart in carts:
        if cart['collided'] == True:
            continue
        if (cart['x'], cart['y']) in cords:
            collision_cords.append((cart['x'], cart['y']))
            print('Collision at %ix%i!' % (cart['x'], cart['y']))
        cords.add((cart['x'], cart['y']))
    if len(collision_cords) == 0:
        return
    for cart in carts:
        if (cart['x'], cart['y']) in collision_cords:
            cart['collided'] = True
    return

map = []
carts = []
y = 0
for row in sys.stdin.read().split('\n'):
    if len(row.strip()) == 0:
        continue
    new_row = []
    for x in range(len(row)):
        if row[x] in ['v', '^', '<', '>']:
            carts.append({'direction': row[x], 'x': x, 'y': y, 'states': ['left', 'straight', 'right'], 'collided': False})
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
    for cart in sorted(carts, key=lambda k: (k['y'], k['x'])):
        if cart['collided']:
            continue
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
            printMap(map)
            print(cart)
            print(tick, cart['x'], cart['y'], map[cart['y']][cart['x']])
            raise Exception('What happend here?')
        moveCart(cart)
        checkCollections(carts)


#    print('Tick: %i' % tick)
#    printMap(map, carts)
    if len(list(filter(lambda x: x['collided'] == False, carts))) <= 1:
        print('At tick %i we have one or no cart left.' % tick)
        print('Remaining cart:')
        print(list(filter(lambda x: x['collided'] == False, carts)))
        break
    tick += 1
