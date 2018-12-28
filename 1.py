import sys

current = 0

for row in sys.stdin.read().strip().split('\n'):
    current += int(row)

print('Final: %i' % current)
