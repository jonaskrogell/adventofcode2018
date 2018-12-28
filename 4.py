import sys


guards = {}

current_guard = 0
sleep_minute = 0
# example syntax: [1518-08-16 23:59] Guard #1489 begins shift
for row in sorted(sys.stdin.read().strip().split('\n')):
    print(row)
    parts = row.split(' ')
    minute = int(parts[1].split(':')[1].replace(']', ''))
    if ' begins shift' in row:
        current_guard = int(parts[3].replace('#', ''))
        print('New guard: %i' % current_guard)
        if current_guard not in guards:
            guards[current_guard] = [0] * 60
    if 'falls asleep' in row:
        sleep_minute = minute
    if 'wakes up' in row:
        for x in range(sleep_minute, minute):
            guards[current_guard][x] += 1

max_guard = 0
max_guard_minutes = 0
for guard in guards:
    if sum(guards[guard]) > max_guard_minutes:
        max_guard = guard
        max_guard_minutes = sum(guards[guard])

single_max_guard = 0
single_max_guard_minute = 0
for guard in guards:
    if max(guards[guard]) > single_max_guard_minute:
        single_max_guard = guard
        single_max_guard_minute = max(guards[guard])

print()
print('Scenario 1')
print('Most asleep guard is %i who sleept %i minutes' % (max_guard, max_guard_minutes))
print('Most common minute: %i' % (guards[max_guard].index(max(guards[max_guard]))))
print('Sum: %i' % (guards[max_guard].index(max(guards[max_guard])) * max_guard))
print()
print('Scenario 2')
print('Most frequent guard is %i' % (single_max_guard))
print('Most common minute: %i' % (guards[single_max_guard].index(max(guards[single_max_guard]))))
print('Sum: %i' % (guards[single_max_guard].index(max(guards[single_max_guard])) * single_max_guard))
