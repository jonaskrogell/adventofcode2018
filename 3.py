import sys


fabric = [x[:] for x in [[0] * 1000] * 1000]


# claim format: #1242 @ 792,499: 10x19
for row in sys.stdin.read().strip().split('\n'):
    parts = row.split(' ')
    claim = parts[0]
    start_x = int(parts[2].split(',')[0])
    start_y = int(parts[2].split(',')[1].replace(':', ''))
    size_x = int(parts[3].split('x')[0])
    size_y = int(parts[3].split('x')[1])

    print(row, claim, start_x, start_y, size_x, size_y)

    for x in range(start_x, start_x + size_x):
        for y in range(start_y, start_y + size_y):
            fabric[x][y] += 1


overlaps = 0
for x in fabric:
    for y in x:
        if y >= 2:
            overlaps += 1

print('Inches with overlap of two or more: %i' % (overlaps))
