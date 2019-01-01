import time


def playMarbles(players, last_marble, score=None):
    print('Playing with %i players and last marble %i' % (players, last_marble))
    player_scores = {}
    current_player = 1
    circle = [0]
    current_marble = 0

    t = time.time()
    for x in range(1, last_marble + 1):
        if t is None or time.time() - t > 10:
            print('%i / %i done (%f%%)' % (x, last_marble, 100.0*x/last_marble))
            t = time.time()
    #    print(current_player, x, circle)
        if x % 23 == 0:
    #        print('23!')
            if current_player not in player_scores:
                player_scores[current_player] = 0
            player_scores[current_player] += x
            remove_marble_position = (current_marble - 7) % len(circle)
            player_scores[current_player] += circle[remove_marble_position]
            circle.pop(remove_marble_position)
            current_marble = remove_marble_position % len(circle)
        else:
            next_marble_position = ((current_marble + 1) % (len(circle))) + 1
            circle.insert(next_marble_position, x)
    #        print('Player %i inserted %i at position %i' % (current_player, x, next_marble_position))
            current_marble = next_marble_position
    #    print(current_player, x, circle)
        current_player = (current_player % players) + 1

#    print('Final scores:')
#    print(player_scores)
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
