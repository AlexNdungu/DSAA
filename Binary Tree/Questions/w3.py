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


    if not nums:
        return None
        
    # Find the middle
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = createTree(nums[:mid])
    node.right = createTree(nums[mid + 1:])
    return node

#Call the fuction
print(createTree(the_array))  

# Now lets display the tree




