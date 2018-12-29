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

def totalDistance(x, y):
    distance_sum = 0
    for id, coordinate in coordinates.items():
        distance_sum += abs(coordinate[0] - x) + abs(coordinate[1] - y)
    return distance_sum


board = {}

on_boarder = set()
print('Board:')
start_x = min_x - max_y
end_x = max_x + max_y
start_y = min_y - max_x
end_y = max_y + max_x
close_coordinates = 0
print('Start, end: X: %i -> %i Y: %i -> %i' % (start_x, end_x, start_y, end_y))
for y in range(start_y, end_y+1):
    for x in range(start_x, end_x+1):
        distance_sum = totalDistance(x, y)
        if distance_sum < 10000:
            print('#', end='')
            close_coordinates += 1
        else:
            print('.', end='')
    print()

print('Sum of area: %i' % (close_coordinates))
