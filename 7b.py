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

workers = {}
for x in range(5):
    workers[x] = {'current_step': None, 'time_remaining': 0}

result = []
time = 0
current_steps = set()
while len(steps) > 0:

    #find candidates
    candidates = set()
    for item in steps:
        # if a worker already works on it, then skip it
        if item in current_steps:
            continue
        if item not in graph:
            candidates.add(item)
        elif len(graph[item]) == 0:
            candidates.add(item)

    # give candidates to free workers
    for step in sorted(candidates):

        for id in workers:
            if workers[id]['current_step'] is None:
                break
        else:
            print(time, 'No free worker')
            continue

        print('With worker %i stepping to %s' % (id, step))
        workers[id]['current_step'] = step
        current_steps.add(step)
        workers[id]['time_remaining'] = 60 + ord(step) - 64

    # progress all workers
    for id in workers:
        if workers[id]['current_step'] is not None:
            workers[id]['time_remaining'] -= 1
            if workers[id]['time_remaining'] == 0:
                step = workers[id]['current_step']
                current_steps.remove(step)
                result.append(step)
                for item in graph:
                    if step in graph[item]:
                        graph[item].remove(step)
                if step in graph:
                    graph.pop(step)
                steps.remove(step)
                workers[id]['current_step'] = None
    print(time, workers)
    time += 1

print('Taken steps:')
print(''.join(result))

print('Took %i seconds' % (time))
