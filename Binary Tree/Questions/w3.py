# Write a Python program to create a Balanced Binary Search Tree (BST) 
# using an array of elements where array elements are sorted in ascending order.

the_array = [1, 2, 3, 4, 5, 6, 7]

#Lets create the TreeNode Class

class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Create a function that can divide this array and set the nodes

def createTree(nums):

    # Find the middle
    mid = len(nums) // 2

    if not nums:
        return None

    node = TreeNode(nums[mid])
    node.left = TreeNode(nums[:mid])
    node.right = TreeNode(nums[mid + 1:])
    return node

#Call the fuction
print(createTree(the_array))  


