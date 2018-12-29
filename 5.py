import sys

polymers = sys.stdin.read().strip()


def test(a, b):
    if a.lower() != b.lower():
        # A does not equal B at all
        return False
    if a.lower() == a and b.upper() == b:
        return True
    if a.upper() == a and b.lower() == b:
        return True
    return False

def collaps(polymers):
    new_polymers = ''
    loops = 0
    while len(new_polymers) != len(polymers):
        loops += 1
    #    print(len(polymers))
        if len(new_polymers) > 0:
            polymers = new_polymers
        new_polymers = ''
        skip_next = False
        for x in range(len(polymers) - 1):
            if skip_next:
                skip_next = False
                continue
            if test(polymers[x], polymers[x+1]):
    #            print('Removes %s and %s' % (polymers[x], polymers[x+1]))
                skip_next = True
                continue
            else:
                new_polymers += polymers[x]
        # Add the last char
        if not skip_next:
            new_polymers += polymers[-1]
    print('Loops: %i' % loops)
    return polymers


collapsed = collaps(polymers)
print('Native: %i' % len(collapsed))

results = {}
for x in 'abcdefgjhijklmnopqrstuvwxyz':
    print('Removing %s' % x)
    removed_polymer = polymers.replace(x, '').replace(x.upper(), '')
    collapsed = collaps(removed_polymer)
    print('%s: %i' % (x, len(collapsed)))
    results[x] = len(collapsed)

print('Length of %i found' % (min(results.values())))
