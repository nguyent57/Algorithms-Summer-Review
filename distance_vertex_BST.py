#IDEA: FIND THE LOWEST common ancestor
#FORMULA: Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)
# lca = lowest common ancestor

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def pathToNode(root, path, k):
    if root is None:
        return False
    path.append(root.key)
    print(path)

    if root.key == k:
        return True
    #CHECK TO SEE WHERE K'S LOCATED, LEFT OR RIGHT
    if (root.left != None and pathToNode(root.left, path, k)) or \
            (root.right !=None and pathToNode(root.right, path, k)):
        return True
    # IF NOT PRESENT IN SUBTREE ROOTED WITH ROOT, RETURN ROOT
    # REMOVE ROOT FROM PATH AND RETURN FALSE
    path.pop()
    return False
def calDist(root, key1, key2):
    if root:
        path1 = []
        pathToNode(root,path1,key1)
        path2=[]
        pathToNode(root, path2, key2)
        i = 0
        while i < len(path1) and  i < len(path2):
            if path1[i] != path2[i]:
                break
            i +=1
        return (len(path1)+len(path2)-2*i)
    return 0


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)

dist = calDist(root, 4, 5)
print ("Distance between node {} & {}: {}".format(4, 5, dist))
