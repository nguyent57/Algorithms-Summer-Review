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
    #RETURN LEFT MOSE NODE
    while (current.left is not None):
        current = current.left
    return current

def delNode(root,key):
    if root is None:
        return root
    #FINDS WHERE THE KEY IS LOCATED BY CHECKING
    #1. IF THE KEY IS LESS THEN ROOT -> ON LEFT,
    #2. ELIF THE KEY IS LARGER THAN ROOT -> RIGHT,
    #3. ELSE THE KEY IS AT ROOT
    if key < root.key:
        root.left = delNode(root.left, key)
    elif key > root.key:
        root.right = delNode(root.right, key)
    else:
        # CHECK TO SEE IF NODE WITH ONLY ONE OR NO CHILD
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # REPLACE NODE WITH SMALLEST VALUE OF RIGHT SUBTREE AKA NEXT VALUE OF NODE
        temp = minVal(root.right)
        # MAKE A COPY TO NEW NODE TEMP
        root.key = temp.key
        # DEL ROOT
        root.right = delNode(root.right, temp.key)
    return root


root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
print("Inorder traversal of the given tree")
inorder(root)
print("\nDelete 20")
root = delNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = delNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = delNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)