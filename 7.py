import sys

graph = {}

steps = set()
for row in sys.stdin.read().strip().split('\n'):
    step_a = row.split(' ')[1]
    step_b = row.split(' ')[7]

    if step_b not in graph:
        graph[step_b] = set()
    graph[step_b].add(step_a)
    steps.add(step_a)
    steps.add(step_b)

print(steps)
print(graph)

result = []
while len(graph) > 0:
    print(graph)

    #find candidates
    candidates = set()
    for item in steps:
        if item not in graph:
            candidates.add(item)
        elif len(graph[item]) == 0:
            candidates.add(item)
    step = sorted(candidates)[0]

    print('Stepping to %s' % (step))
    result.append(step)

    for item in graph:
        if step in graph[item]:
            graph[item].remove(step)
    if step in graph:
        graph.pop(step)
    steps.remove(step)
    print('Removed %s' % (step))
    print(graph)

print('Taken steps:')
print(''.join(result))
