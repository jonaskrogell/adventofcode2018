import sys

twos = 0
threes = 0

for row in sys.stdin.read().strip().split('\n'):
    letters = {}
    for letter in row:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    if 2 in letters.values():
        twos += 1
    if 3 in letters.values():
        threes += 1

print('Twos: %i Threes: %i' % (twos, threes))
print('Twos x Thress = %i' % (twos * threes))
