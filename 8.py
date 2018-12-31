import sys
import pprint

nodes = []

for row in sys.stdin.read().strip().split(' '):
    nodes.append(int(row))

def parseNodes(node_index, data):
    node_index += 1
    node = {}
    node['childs'] = []
    node['meta'] = []
    node['index'] = node_index
    node['child_quantity'] = data.pop(0)
    node['metadata_quantity'] = data.pop(0)
    for child in range(node['child_quantity']):
        node_index, data, child = parseNodes(node_index, data)
        node['childs'].append(child)
    for metadata in range(node['metadata_quantity']):
        meta = data.pop(0)
        node['meta'].append(meta)
    return node_index, data, node


def sumMeta(tree, s = 0):
    s += sum(tree['meta'])
    for child in tree['childs']:
        s += sumMeta(child)
    return s


def checksumMeta(tree, s = 0):
    if tree['child_quantity'] == 0:
        return sum(tree['meta'])
    for meta in tree['meta']:
        if meta > tree['child_quantity']:
            continue
        s += checksumMeta(tree['childs'][meta - 1])
    return s


print('Input nodes: %s' % nodes)
node_index, data, tree = parseNodes(0, nodes)
print('Final node_index: %i' % node_index)
print('Tree:')
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(tree)

print('Part1-sum of meta: %i' % sumMeta(tree))
print('Part2-sum of meta: %i' % checksumMeta(tree))
