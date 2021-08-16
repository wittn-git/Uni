#class for binary search tree
class Tree:

    def __init__(self, values):
        self.root = None
        for v in values: self.insert(v)

    def insert(self, value):
        if self.root == None: self.root = TreeNode(value)
        else: self.root.insert(value)
    
    def get_height(self):
        return self.root.get_height()

#class for node of binary tree
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    def insert(self, value):
        if self.value > value:
            if self.left == None: self.left = TreeNode(value)
            else: self.left.insert(value)
        elif (self.value < value):
            if self.right == None: self.right = TreeNode(value)
            else: self.right.insert(value)
    
    def get_height(self):
        if self.left == None:
            if self.right == None:
                return 1
            else:
                return 1+self.right.get_height()
        else:
            if self.right == None:
                return 1+self.left.get_height()
            else:
                return 1+max(self.right.get_height(), self.left.get_height())

#returns all keys in binary search tree tree, which have values between a and b
def search(tree, a, b):
    return h(tree.root, a, b)

#helper function
def h(node, a, b):
    if node == None: return [] # if node does not exist, do not att values
    if node.value < a: # if node value is smaller then lower bound, just search right subtree
        return h(node.right, a, b)
    if node.value > b: # if node value is bigger then lower bound, just search left subtree
        return h(node.left, a, b)
    return [node.value] + h(node.left, a,b) + h(node.right, a,b) # if node is in range, add node value and search both subtrees