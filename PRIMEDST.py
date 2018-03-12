from math import sqrt
from collections import deque

def counter_mult(c1, c2):
    result = deque([0] * (len(c1) * len(c2)))
    for i in xrange(0, len(c1)):
        for j in xrange(0, len(c2)):
            result[i+j] = c1[i] * c2[j]

    return result

def counter_inc(c, i):
    for _ in xrange(0, i):
        c.appendleft(0)

    return c

def counter_add(c1, c2):
    return deque(map(lambda a,b: (a or 0)+(b or 0), c1, c2))

def is_prime(c):
    if c == 1:
        return False

    for divider in xrange(2, int(sqrt(c)) + 1):
        mod = c % divider
        if mod == 0:
            return False

    return True

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

        self.depth_counter = None
        self.paths = None

    def set_parent(self, parent_node):
        self.parent = parent_node
        parent_node.children.append(self)

    def __repr__(self):
        if self.parent:
           return 'Node({}<{})'.format(self.value, self.parent.value)
        else:
            return 'Node({})'.format(self.value)

    def prepare_depth_counters(self):
        to_prepare = []
        current = [self]
       
        while current:
            to_prepare += current
            current = sum((n.children for n in current), [])

        for node in reversed(to_prepare):
            print '.'
            print node
            result = None
            for c in node.children:
                if result is None:
                    result = counter_inc(c.find_depth_counter(), 1)
                    result[0] += 1
                else:
                    result = counter_add(result, counter_inc(c.find_depth_counter(), 1))

            if result is None:
                result = deque([1])

            node.depth_counter = result

    def prepare_paths(self):
        self.prepare_depth_counters()

        to_prepare = []
        current = [self]
       
        while current:
            to_prepare += current
            current = sum((n.children for n in current), [])

        for node in reversed(to_prepare):
            print node
            result = deque()

            for i in range(0, len(node.children)):
                i_depth = counter_inc(node.children[i].find_depth_counter(), 1)
                result = counter_add(result, i_depth)
                result = counter_add(result, counter_inc(node.children[i].find_paths(), 1))
                print len(result)

                for j in range(i + 1, len(node.children)):
                    j_depth = counter_inc(node.children[j].find_depth_counter(), 1)
                    result = counter_add(result, counter_mult(i_depth, j_depth))
            
            node.paths = result

    def find_depth_counter(self):
        if self.depth_counter is None:
            raise ValueError('Prepare first!')

        return self.depth_counter

    def find_paths(self):
        if self.paths is None:
            raise ValueError('Prepare first!')

        return self.paths


class Tree(object):
    def __init__(self, nodes, root):
        self.nodes = nodes
        self.root = root

    def __repr__(self):
        return 'Tree(root={}, nodes={})'.format(self.root, self.nodes.values())

    @classmethod
    def create_from_input(cls):
        nodes = {}
        root_candidates = set()

        _ = raw_input()
        while True:
            try:
                node_value_pair = map(int, raw_input().split(' '))
            except EOFError:
                break

            node_pair = [nodes.setdefault(v, Node(v)) for v in node_value_pair]

            linked = False
            for node, another_node in node_pair, reversed(node_pair):
                if not node.parent:
                    root_candidates.add(node)
                    if not linked:
                        node.set_parent(another_node)
                        root_candidates.remove(node)
                        linked = True
            assert linked

        assert len(root_candidates) == 1

        return cls(nodes, *root_candidates)

tree = Tree.create_from_input()

tree.root.prepare_paths()

paths = tree.root.find_paths()

prime_paths = 0
all_paths = 0
for length in xrange(0, len(paths)):
    if length == 0:
        next
    if is_prime(length):
        prime_paths += paths[length]

    all_paths += paths[length]

print 1.0 * prime_paths / all_paths
