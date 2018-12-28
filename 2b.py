import sys

def isSimilar(box1, box2):
    matches = 0
    same = ''
    for x in range(len(box1)):
        if box1[x] == box2[x]:
            matches += 1
            same += box1[x]
    if matches >= len(box1) - 1:
        print('Same letters: %s' % same)
        return True
    else:
        return False

boxes = []

for row in sys.stdin.read().strip().split('\n'):
    for box in boxes:
        if isSimilar(box, row):
            print('Similar boxes found: %s %s' % (box, row))
            sys.exit(0)
    boxes.append(row)
