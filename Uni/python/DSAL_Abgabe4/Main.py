import random

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

def h(node, a, b):
    if node == None: return [], 1
    if node.value < a:
        r = h(node.right, a, b)
        return r[0], r[1]+2
    if node.value > b:
        r = h(node.left, a, b)
        return r[0], r[1]+2
    r1, r2 = h(node.left, a,b), h(node.right, a,b)
    return [node.value] + r1[0] + r2[0], r1[1]+r2[1]

entries = []
for i in range(1000):
    r = random.randint(0,10000)
    entries.append(r)
tree = Tree(entries)
result, n = search(tree, random.randint(0, 5000), random.randint(5000, 10000))
print('target runtime: O({})'.format(tree.get_height()+len(result)))
print('runtime: {}'.format(n))
print(result)