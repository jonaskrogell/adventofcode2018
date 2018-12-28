import sys

change_list = []

for row in sys.stdin.read().strip().split('\n'):
    change_list.append(int(row))

freqs = set()
current = 0

found = False
while not found:
    for change in change_list:
        current += change
        if current in freqs:
            print('Found repetition: %i' % current)
            found = True
            break
        freqs.add(current)
