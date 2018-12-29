import sys

coordinates = {}

min_x = None
min_y = None
max_x = None
max_y = None
id = 0
for row in sys.stdin.read().strip().split('\n'):
    x = int(row.split(',')[0])
    y = int(row.split(',')[1])
    if min_x is None or x < min_x: min_x = x
    if max_x is None or x > max_x: max_x = x
    if min_y is None or y < min_y: min_y = y
    if max_y is None or y > max_y: max_y = y
    coordinates[id] = (x, y)
    id += 1

print('Borders: %ix%i - %ix%i' % (min_x, min_y, max_x, max_y))

def findClosetsCoordinate(x, y):
    most_close = None
    most_close_distance = None
    most_close_count = 0
    for id, coordinate in coordinates.items():
        distance = abs(coordinate[0] - x) + abs(coordinate[1] - y)
        if most_close_distance is None or distance < most_close_distance:
            most_close_distance = distance
            most_close = id
            most_close_count = 1
        elif distance == most_close_distance:
            most_close_count += 1
    if most_close_count > 1:
        return False
    return most_close


board = {}

on_boarder = set()
#print('Board:')
start_x = min_x - max_y
end_x = max_x + max_y
start_y = min_y - max_x
end_y = max_y + max_x
print('Start, end: X: %i -> %i Y: %i -> %i' % (start_x, end_x, start_y, end_y))
for y in range(start_y, end_y+1):
    for x in range(start_x, end_x+1):
        id = findClosetsCoordinate(x, y)
        if id is False:
#            print('.', end='')
            continue
        if x in [start_x, end_x] or y in [start_y, end_y]:
            on_boarder.add(id)
        if id not in board:
            board[id] = 0
        board[id] += 1
#        print(id, end='')
#    print()

print(board)
print(on_boarder)

for id, value in sorted(board.items(), key=lambda kv: kv[1], reverse=True):
    if id in on_boarder:
        continue
    print('Result id %i value %i' % (id, value))
    break
