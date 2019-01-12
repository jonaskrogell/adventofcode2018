def printScoreboard(scoreboard, elves):
    for pos in range(len(scoreboard)):
        for elve in elves:
            if elve == pos:
                print('<%i>  ' % scoreboard[pos], end='')
                break
        else:
            print('%i  ' % scoreboard[pos], end='')
    print('')


def doRecepies(recepies, search=False):
    print('Doing %s recepies, search=%s' % (str(recepies), str(search)))
    elves = []
    for elve in range(2):
        elves.append(elve)
    scoreboard = [3, 7]
    while True:
#        printScoreboard(scoreboard, elves)
        sum = 0
        for elve in elves:
            sum += scoreboard[elve]
        for digit in str(sum):
            scoreboard.append(int(digit))
        for elve in range(len(elves)):
            elves[elve] = (elves[elve] + scoreboard[elves[elve]] + 1) % len(scoreboard)
        if not search:
            if len(scoreboard) >= recepies + 10:
                return ''.join(map(str, scoreboard[recepies:recepies+10]))
        else:
            if recepies in ''.join(map(str, scoreboard[-(len(str(sum))+len(recepies)):])):
                return ''.join(map(str, scoreboard)).index(recepies)
#    printScoreboard(scoreboard, elves)

print(doRecepies(9) == '5158916779')
print(doRecepies(5) == '0124515891')
print(doRecepies(18) == '9251071085')
print(doRecepies(2018) == '5941429882')

print('Answer 14a: %s' % doRecepies(681901))

print(doRecepies('51589', search=True) == 9)
print(doRecepies('01245', search=True) == 5)
print(doRecepies('92510', search=True) == 18)
print(doRecepies('59414', search=True) == 2018)

print('Answer 14b: %s' % doRecepies('681901', search=True))
