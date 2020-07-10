class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def isSumTree(root):
    # ID ROOT DOES NOT EXIST -> RETURN NOTHING
    if root is None:
        return 0
    # IF LEFT AND RIGHT LEAF DO NOT EXIST -> RETURN ROOT KEY (BY ITSELF)
    if (root.left is None and root.right is None):
        return (root.key)
    # IF ROOT KEY IS EQUAL TO THE SUM OF LEFT AND RIGHT  -> RETURN IT
    if root.key == isSumTree(root.left)+isSumTree(root.right):
        return(2*(root.key))
    return float('-inf')
root = Node(44)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

if isSumTree(root) != float('-inf'):
    print('yes', isSumTree(root.left)+isSumTree(root.right))
else:
    print('no')
