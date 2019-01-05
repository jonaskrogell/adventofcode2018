import sys

serial = int(sys.stdin.read().strip())

def getPower(x, y, serial, correct_power=None):
    #Find the fuel cell's rack ID, which is its X coordinate plus 10.
    power = x + 10
    #Begin with a power level of the rack ID times the Y coordinate.
    power = power * y
    #Increase the power level by the value of the grid serial number (your puzzle input).
    power += serial
    #Set the power level to itself multiplied by the rack ID.
    power = power * (x + 10)
    #Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    if abs(power) >= 100:
#        power = int(str(power)[-3])
        power = int(power/100 % 10)
    else:
        power = 0
    #Subtract 5 from the power level.
    power -= 5

    if correct_power is not None:
        if power != correct_power:
            raise Exception('Testing failed for %i,%i serial %i with expected power %i, but got %i.' % (x, y, serial, correct_power, power))

    return power

# tests
getPower(3,5, 8, 4)
getPower(122,79, 57, -5)
getPower(217,196, 39, 0)
getPower(101,153, 71, 4)


max_sum = None
max_x = None
max_y = None
for y in range(1, 299):
    for x in range(1, 299):
        # do square check
        s = 0
        for s_y in range(3):
            for s_x in range(3):
                s += getPower(x + s_x, y + s_y, serial)
        if max_sum is None or s > max_sum:
            max_sum = s
            max_x = x
            max_y = y

print('Max sum of %i found at %i,%i' % (max_sum, max_x, max_y))
