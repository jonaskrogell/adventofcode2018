
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
    power = int(power/100 % 10)
    #Subtract 5 from the power level.
    power -= 5
    if correct_power is not None:
        if power != correct_power:
            raise Exception('Testing failed for %i,%i serial %i with expected power %i, but got %i.' % (x, y, serial, correct_power, power))
    return power


def getGrid(serial):
    grid = []
    for y in range(300 + 1):
        row = []
        for x in range(300 + 1):
            row.append(getPower(x, y, serial))
        grid.append(row)
    return grid


def getMaxSquare(grid, size, correct_sum=None, correct_x=None, correct_y=None):
    max_sum = None
    max_x = None
    max_y = None

    for x in range(1, 300 - size + 2):
        prev_s = None
        for y in range(1, 300 - size + 2):
            if prev_s is None:
                # do square check from scratch
                s = 0
                for s_y in range(size):
                    s += sum(grid[y + s_y][x : x + size])
            else:
                s = prev_s
                s -= sum(grid[y - 1][x : x + size])
                s += sum(grid[y + size - 1][x : x + size])

            prev_s = s
            if max_sum is None or s > max_sum:
                max_sum = s
                max_x = x
                max_y = y
    if correct_sum is not None:
        if max_sum != correct_sum or max_x != correct_x or max_y != correct_y:
            raise Exception('Testing failed for size %i. Sum: %i %i X: %i %i Y: %i %i' % (size, correct_sum, max_sum, correct_x, max_x, correct_y, max_y))
    return max_sum, max_x, max_y, size


# tests
getPower(3, 5, 8, 4)
getPower(122, 79, 57, -5)
getPower(217, 196, 39, 0)
getPower(101, 153, 71, 4)

getMaxSquare(getGrid(18), 3, 29, 33, 45)
getMaxSquare(getGrid(42), 3, 30, 21, 61)
getMaxSquare(getGrid(18), 16, 113, 90,269)
getMaxSquare(getGrid(42), 12, 119, 232,251)
print('Tests passed.')

# Jonas serial
grid = getGrid(7803)
max_sum, max_x, max_y, size = getMaxSquare(grid, 3)
print('Max sum of %i found at %i,%i of square size %i' % (max_sum, max_x, max_y, size))

print('Brute force the size:')
for size in range(300):
    max_sum, max_x, max_y, size = getMaxSquare(grid, size)
    print('Max sum of %i found at %i,%i of square size %i' % (max_sum, max_x, max_y, size))
