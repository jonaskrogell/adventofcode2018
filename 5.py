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
print('Final:')
print(polymers)
print(len(polymers))
