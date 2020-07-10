#IDEA: BST ARE SORT -> RIGHT MOST IS THE LARGEST VALUE
# -> SECOND LARGEST CAN BE:
    #1. PARENT OF THE LARGEST
    #2. LARGEST HAS LEFT SUBTREE
    #3. SECOND LARGEST IS THE PARENT OF LARGEST
                    #AND SECOND LARGEST HAS NO LEFT SUBTREE
#PLAN: FIND THE LARGEST VALUE -> SECOND LARGEST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(node, key):
    # IF THE TREE IS EMPTY, RETURN THE NODE
    if node is None:
        return Node(key)
    # RECUR: IF KEY < NODE -> INSERT LEFT, ELSE INSERT RIGHT
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def largest(node):
        current = node
        while current.right is not None:
            current = current.right
        return current.key
def secondLargest(node):
    # CHECK IF ROOT EXISTS
    if (node is None or (node.left is None and node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')
    current = node
    while current:
        # CASE 2: CURRENT IS LARGEST AND HAS A LEFT SUBTREE
        # 2ND LARGEST IS THE LATEST IN THAT SUBTREE
        if current.left and not current.right: # IF THERE IS LEFT SUBTREE AND NO RIGHT TREE
            return largest(current.left)       # RETURN THE LARGEST VALUE OF THAT
        # CASE 1: CURRENT IS THE PARENT OF LARGEST AND LARGEST HAS NO CHILD -> CURRENT IS THE 2ND LARGEST
        if (current.right and not current.right.left and # IF CURRENT HAS NO LEFT CHILD
                              not current.right.right):  # OR NO RIGHT CHILD
            return current.key                           # RETURN THE CURRENT VALUE
        current = current.right
root = None
keys = [5,3,4,1,2]
for key in keys:
    root = insert(root, key)

print(secondLargest(root))