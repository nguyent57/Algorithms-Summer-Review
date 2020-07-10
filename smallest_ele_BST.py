class Node:
    # CONSTRUCTOR TO CREATE NEW NODE
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#FUNCTION TO DO INORDER TRAVERSAL OF BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

#FUNCTION TO INSERT NEW NODE
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

#FUNCTION TO RETURN MIN VALUE OF A NON-EMPTY BST
# THE ENTIRE TREE DOES NOT NEED TO BE SEARCHED
def minVal(node):
    current = node
    #RETURN LEFT MOST LEAF
    while (current.left is not None):
        current = current.left
    return current.key
root = None
keys = [5,3,4,1,2]
for key in keys:
    root = insert(root, key)
print(inorder(root))
print(minVal(root))