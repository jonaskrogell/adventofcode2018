import sys

rows = sys.stdin.read().strip().split('\n')
pots = rows[0].split(':')[1].strip()
spreads = {}
for row in rows[1:]:
    if len(row.strip()) > 0:
        pattern = row.strip().split(' ')[0]
        result = row.strip().split(' ')[2]
        spreads[pattern] = result


def getSum(pots, offset):
    s = 0
    for x in pots:
        if x == '#':
            s += offset
        offset += 1
    return s


offset = 0
print(0, pots)
for gen in range(1, 20 + 1):
    # pad on empty pots
    while pots[:5] != '.....':
        pots = '.' + pots
        offset -= 1
    while pots[-5:] != '.....':
        pots = pots + '.'
    ng_pots = '..'
    for nr in range(2, len(pots) - 2):
        pattern = pots[nr - 2:nr + 3]
        if pattern in spreads:
            ng_pots += spreads[pattern]
        else:
            ng_pots += '.'

    if pots.strip('.') == ng_pots.strip('.'):
        print('After gen %i they are identical' % gen)
        break
    pots = ng_pots
    print(gen, pots)
    if gen % 1000 == 0:
#        print(gen, pots)
        print('Sum: %i' % (getSum(pots, offset)))


print('Sum: %i' % (getSum(pots, offset)))
