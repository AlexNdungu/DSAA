# Firts create a tree

class TreeNode:

    def __init__(self, key):
        # instanciate
        self.key = key
        self.left = None
        self.right = None

# The array that we wll create the tree with

theArray = [1, 2, 3, 4, 5, 6]

# Now fill the tree with values

def createTree(collection):
    
    if not collection:
        return None
    
    #sort the array
    collection.sort()
    
    # Now divide the array to two
    low = 0
    high = len(collection) - 1

    mid = (low + high) // 2

    #print(mid)

    node = TreeNode(collection[mid])
    node.left = createTree(collection[:mid])
    node.right = createTree(collection[mid + 1:])
    return node

# Call the fuction
tree = createTree(theArray)

#print(tree)


#Lets perform a inorder transversal
from transvarse import inorderTransversal,preorderTransversal, postorderTransversal

print(inorderTransversal(tree))

# Preorder transversal
print(preorderTransversal(tree))

# postorder transversal
print(postorderTransversal(tree))

# Find the height of the tree

from maximum import maxRoute

print(maxRoute(tree))


