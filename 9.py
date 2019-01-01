import time
import collections

def playMarbles(players, last_marble, score=None):
    print('Playing with %i players and last marble %i' % (players, last_marble))
    player_scores = {}
    current_player = 1
    circle = collections.deque([0])
    current_marble = 0

    t = time.time()
    for x in range(1, last_marble + 1):
        if x % 1000 == 0 and time.time() - t > 1:
            print('%i / %i done (%f%%)' % (x, last_marble, 100.0*x/last_marble))
            t = time.time()
#        print(current_player, x, circle)
        if x % 23 == 0:
            if current_player not in player_scores:
                player_scores[current_player] = 0
            player_scores[current_player] += x
            circle.rotate(7)
            player_scores[current_player] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(x)
        current_player = (current_player % players) + 1

    m = max(player_scores.values())
    if score is not None:
        if m == score:
            print('Okay. Score as expected: %i' % (m))
        else:
            print('Error, unexpected score. Expected %i but got %i' % (score, m))
    else:
        print('Got score: %i' % (m))
    return m

# test data
playMarbles(9, 25, 32)
playMarbles(10, 1618, 8317)
playMarbles(13, 7999, 146373)
playMarbles(17, 1104, 2764)
playMarbles(21, 6111, 54718)
playMarbles(30, 5807, 37305)

# my input:
playMarbles(455, 71223)
playMarbles(455, 71223 * 100)
