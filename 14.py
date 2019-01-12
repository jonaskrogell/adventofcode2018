def printScoreboard(scoreboard, elves):
    for pos in range(len(scoreboard)):
        for elve in elves:
            if elve == pos:
                print('<%i>  ' % scoreboard[pos], end='')
                break
        else:
            print('%i  ' % scoreboard[pos], end='')
    print('')

def doRecepies(recepies):
    print('Doing %i recepies' % recepies)
    elves = []
    for elve in range(2):
        elves.append(elve)
    scoreboard = [3, 7]
    while True:
#        printScoreboard(scoreboard, elves)
        sum = 0
        for elve in elves:
            sum += scoreboard[elve]
        # nrs = []
        # while sum > 0:
        #     nrs.append(sum % 10)
        #     sum = int((sum - sum % 10)/10)
        # nrs.reverse()
        # for nr in nrs:
        #     scoreboard.append(nr)
        for digit in str(sum):
            scoreboard.append(int(digit))
        for elve in range(len(elves)):
            elves[elve] = (elves[elve] + scoreboard[elves[elve]] + 1) % len(scoreboard)

        if len(scoreboard) >= recepies + 10:
            break
#    printScoreboard(scoreboard, elves)
    return ''.join(map(str, scoreboard[recepies:recepies+10]))

print(doRecepies(9) == '5158916779')
print(doRecepies(5) == '0124515891')
print(doRecepies(18) == '9251071085')
print(doRecepies(2018) == '5941429882')

print(doRecepies(681901))
