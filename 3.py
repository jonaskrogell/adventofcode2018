import sys


fabric = [x[:] for x in [[0] * 1000] * 1000]

claims = sys.stdin.read().strip().split('\n')

# claim format: #1242 @ 792,499: 10x19
for claim in claims:
    parts = claim.split(' ')
    claim_id = parts[0]
    start_x = int(parts[2].split(',')[0])
    start_y = int(parts[2].split(',')[1].replace(':', ''))
    size_x = int(parts[3].split('x')[0])
    size_y = int(parts[3].split('x')[1])

    for x in range(start_x, start_x + size_x):
        for y in range(start_y, start_y + size_y):
            fabric[x][y] += 1

# hack copy-paste checking
for claim in claims:
    parts = claim.split(' ')
    claim_id = parts[0]
    start_x = int(parts[2].split(',')[0])
    start_y = int(parts[2].split(',')[1].replace(':', ''))
    size_x = int(parts[3].split('x')[0])
    size_y = int(parts[3].split('x')[1])

    clean = True
    for x in range(start_x, start_x + size_x):
        for y in range(start_y, start_y + size_y):
            if fabric[x][y] != 1:
                clean = False
    if clean:
        print('Claim %s is a clean claim' % (claim_id))


overlaps = 0
for x in fabric:
    for y in x:
        if y >= 2:
            overlaps += 1

print('Inches with overlap of two or more: %i' % (overlaps))
