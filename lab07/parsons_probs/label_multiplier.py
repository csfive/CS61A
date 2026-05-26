def label_multiplier(t, val):
    """
    Given a tree t, mutate t so that all of the tree's
    labels are multiplied by the argument val.

    >>> t1 = Tree(2, [Tree(4, [Tree(6)]), Tree(8)])
    >>> label_multiplier(t1, 10)
    >>> t1
    Tree(20, [Tree(40, [Tree(60)]), Tree(80)])
    >>> t2 = Tree(10, [Tree(9), Tree(8, [Tree(7), Tree(6)]), Tree(5, [Tree(4), Tree(3), Tree(2)])])
    >>> label_multiplier(t2, 3)
    >>> t2
    Tree(30, [Tree(27), Tree(24, [Tree(21), Tree(18)]), Tree(15, [Tree(12), Tree(9), Tree(6)])])
    """
    "*** YOUR CODE HERE ***"


class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
