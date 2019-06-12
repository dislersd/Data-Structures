class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Dont forget to wrap the value in a node

        # 1. Compare the element againt current value
        # 2. Based on the result of the comparison go left or right
        # 3. If we find an empty spot park element there
        # 4. Otherwise go back to step 1

        # Base case?
        # base: we have found an empty spot where we can add the value

        if value < self.value:
            # if value is less, we go left
            # if there is no left child, we can put node here
            if not self.left:
                self.left = BinarySearchTree(value)
            # recurse on the left child
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # 1. Compare target to root (self.value)
        # 2. Based on result of comparison go left or right or return true if equal return false
        # 3. If we find target return true
        # 4. Otherwise go back to step 1

        # base case: if target = value return true

        # if target is root return true
        if target == self.value:
            return True
        # if target is less than root check left subtree
        if target < self.value:
            if not self.left:
                return False
            # if target return true
            elif target == self.left.value:
                return True
            # or else recurse on left child
            else:
                self.left.contains(target)
        # else if target is greater than root check right subtree
        if target > self.value:
            if not self.right:
                return False
            # if target return true
            elif target == self.right.value:
                return True
            # or else recurse on right child
            else:
                self.right.contains(target)
        else:
            return False

    def get_max(self):
        # 1. root node is cur max
        # 2. If there is no right return cur max
        # 3. recurse until no more right and return value

        cur_max = self.value
        if not self.right:
          return cur_max
        else:
         return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
