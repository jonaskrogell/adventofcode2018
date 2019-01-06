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
total_gens = 50000000000
print(0, pots)
for gen in range(1, total_gens + 1):
    # pad on empty pots
#    print(pots)
    while pots[:3] != '...':
        pots = '.' + pots
#        print('left padding')
        offset -= 1
    while pots[-3:] != '...':
        pots = pots + '.'
#        print('right padding')
#    print(pots)
    ng_pots = '..'
    for nr in range(2, len(pots) - 2):
        pattern = pots[nr - 2:nr + 3]
        if pattern in spreads:
            ng_pots += spreads[pattern]
        else:
            ng_pots += '.'

    if pots.strip('.') == ng_pots.strip('.'):
        print('After gen %i they are identical' % gen)
        p = pots.strip('.')
        print('Shift: %i' % (ng_pots.index(p) - pots.index(p) ))
        offset += (ng_pots.index(p) - pots.index(p) ) * ( total_gens - gen + 1)
        break
    pots = ng_pots
    print(gen, offset, pots)
    if gen == 20:
        print(gen, pots)
        print('Round 20 Sum: %i' % (getSum(pots, offset)))


print('Sum after %i rounds: %i' % (total_gens, getSum(pots, offset)))
