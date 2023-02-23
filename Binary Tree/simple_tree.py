# Create a simple binary tree

class TreeNode:

    def __init__(self, key):
        
        self.key = key
        self.right = None
        self.left = None

#Create objects representing nodes in the above tree

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print(node0.key)

#Set the left and right node

node0.left = node1
node0.right = node2

#Lets track the tree
tree = node0

