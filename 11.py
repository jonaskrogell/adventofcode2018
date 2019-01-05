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


def getMaxSquare(size, serial, correct_sum=None, correct_x=None, correct_y=None):
    max_sum = None
    max_x = None
    max_y = None
    for y in range(1, 300 - size + 2):
        prev_s = None
        for x in range(1, 300 - size + 2):
            if prev_s is None:
                # do square check from scratch
                s = 0
                for s_y in range(size):
                    for s_x in range(size):
                        s += getPower(x + s_x, y + s_y, serial)
            else:
                s = prev_s
                for s_y in range(size):
                    s -= getPower(x - 1 , y + s_y, serial)
                    s += getPower(x + size - 1, y + s_y, serial)
            prev_s = s
            if max_sum is None or s > max_sum:
                max_sum = s
                max_x = x
                max_y = y
    if correct_sum is not None:
        if max_sum != correct_sum or max_x != correct_x or max_y != correct_y:
            raise Exception('Testing failed for size %i serial %i. Sum: %i %i X: %i %i Y: %i %i' % (size, serial, correct_sum, max_sum, correct_x, max_x, correct_y, max_y))
    return max_sum, max_x, max_y, size


# tests
getPower(3,5, 8, 4)
getPower(122,79, 57, -5)
getPower(217,196, 39, 0)
getPower(101,153, 71, 4)

getMaxSquare(3, 18, 29, 33, 45)
getMaxSquare(3, 42, 30, 21, 61)
getMaxSquare(16, 18, 113, 90,269)
getMaxSquare(12, 42, 119, 232,251)
print('Tests passed.')

# Jonas serial
serial = 7803
max_sum, max_x, max_y, size = getMaxSquare(3, serial)
print('Max sum of %i found at %i,%i of square size %i' % (max_sum, max_x, max_y, size))

print('Brute force the size:')
for size in range(300):
    max_sum, max_x, max_y, size = getMaxSquare(size, serial)
    print('Max sum of %i found at %i,%i of square size %i' % (max_sum, max_x, max_y, size))
