import sys
import time

points = []


for row in sys.stdin.read().strip().split('\n'):
    pos = row.split('<')[1].split('>')[0].split(',')
    vel = row.split('<')[2].split('>')[0].split(',')
    light = {'x': int(pos[0]), 'y': int(pos[1]), 'velocity_x': int(vel[0]), 'velocity_y': int(vel[1])}
    points.append(light)

def printPoints(points):
    min_x = points[0]['x']
    min_y = points[0]['y']
    max_x = min_x
    max_y = min_y
    visible_points = set()
    for point in points:
        min_x = min(min_x, point['x'])
        min_y = min(min_y, point['y'])
        max_x = max(max_x, point['x'])
        max_y = max(max_y, point['y'])
        visible_points.add((point['x'], point['y']))
    is_message = True
    for x, y in visible_points:
        # if a single point has no neighbors its not a message
        if (x + 1, y) in visible_points: continue
        if (x - 1, y) in visible_points: continue
        if (x, y + 1) in visible_points: continue
        if (x, y - 1) in visible_points: continue
        if (x + 1, y + 1) in visible_points: continue
        if (x - 1, y - 1) in visible_points: continue
        if (x + 1, y - 1) in visible_points: continue
        if (x - 1, y + 1) in visible_points: continue
        is_message = False
        break

    if is_message:
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                if (x, y) in visible_points:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    return is_message

def movePoints(points):
    for point in points:
        point['x'] += point['velocity_x']
        point['y'] += point['velocity_y']

t = 0
while True:
#    print(t)
    is_message = printPoints(points)
#    print('Is message: %s' % is_message)
    if is_message:
        break
    t += 1
    movePoints(points)
#    time.sleep(1)
#print(points)
