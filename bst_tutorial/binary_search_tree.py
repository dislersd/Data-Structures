class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
            else:
                self._insert(value, cur_node.left_child)
        if value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)

    def contains(self, target):
        pass
        # compare value to root of tree
        # if value is less than root traverse down left
        # if value is more than root traverse down right
        #

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
