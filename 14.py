def printScoreboard(scoreboard, elves):
    for pos in range(len(scoreboard)):
        for elve in elves:
            if elves[elve] == pos:
                print('<%i>  ' % scoreboard[pos], end='')
                break
        else:
            print('%i  ' % scoreboard[pos], end='')
    print('')

def doRecepies(nr):
    print('Doing %i recepies' % nr)
    elves = {}
    for elve in range(2):
        elves[elve] = elve
    scoreboard = [3, 7]
    while True:
#        printScoreboard(scoreboard, elves)
        sum = 0
        for elve in elves:
            sum += scoreboard[elves[elve]]
        for digit in str(sum):
            scoreboard.append(int(digit))
        for elve in elves:
            elves[elve] = (elves[elve] + scoreboard[elves[elve]] + 1) % len(scoreboard)

        if len(scoreboard) >= nr + 10:
            break
#    printScoreboard(scoreboard, elves)
    return ''.join(map(str, scoreboard[nr:nr+10]))

print(doRecepies(9) == '5158916779')
print(doRecepies(5) == '0124515891')
print(doRecepies(18) == '9251071085')
print(doRecepies(2018) == '5941429882')

print(doRecepies(681901))
