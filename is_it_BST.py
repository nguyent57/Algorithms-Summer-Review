# Data structure to store a Binary Search Tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Recursive function to insert a key into BST
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


# Function to determine if given Binary Tree is a BST or not by keeping a
# valid range (starting from [-INFINITY, INFINITY]) and keep shrinking
# it down for each node as we go down recursively
def isBST(node, minKey, maxKey):
    # base case
    if node is None:
        return True

    # if node's value fall outside valid range
    if node.key < minKey or node.key > maxKey:
        return False

    # recursively check left and right subtrees with updated range
    else:

        return isBST(node.left, minKey, node.key) and \
               isBST(node.right, node.key, maxKey)


# Function to determine if given Binary Tree is a BST or not
def checkForBST(root):
    if isBST(root, float('-inf'), float('inf')):
        print("This is a BST.")
    else:
        print("This is NOT a BST")


def swap(root):
    root.left,root.right = root.right, root.left


root = None
keys = [1,2,3,4,5]
for key in keys:
    root = insert(root, key)
# swap left and right nodes -> makes it not in order -> not a BST
swap(root)
checkForBST(root)