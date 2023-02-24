# Search in a Binary Search Tree

# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
# If such a node does not exist, return null.

# What I understand:
    # 1. Create a BST.
    # 2. Given a value = val, find the subtree that val is attached and return the subtree

# Test Cases:

tests = []

# Test case 1: Tree contains the value val

tests.append({
    'input':{
        'root' : [4,2,7,1,3],
        'val' : 2
    },
    'output' : [2,1,3]
})

# Sudo Code Section
    # 1. Sort the array provided in ascending order
    # 2. Create a fuction that:
        # Divides the array to left and right subtree
        # Repeat the above as you create the nodes
    # 3. Create another function that searches through the tree:
        #     


# Write the code and debug

# Create tree structure
class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Fuction that fills in the array to tree

def arrayToTree(nums):

    if not nums:
        return None

    nums.sort()

    print(nums)

    #Lets find the root and add it
    mid = len(nums) // 2

    #Create the tree 
    root = TreeNode(nums[mid])
    #left side
    root.left = arrayToTree(nums[:mid])
    #right side
    root.right = arrayToTree(nums[mid + 1:])
    return root

# Now lets create the tree

test = {
    'input':{
        'root' : [4,2,7,1,3],
        'val' : 2
    },
    'output' : [2,1,3]
}

#print(test['input']['root'])

arrayToTree(test['input']['root'])    


# Leet Code answer
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val==val:
            return root
        if root.val<val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)