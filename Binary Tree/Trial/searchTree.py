# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
# If such a node does not exist, return null.

def findVal(root,val):

    result = []

    if root is None:

        return []
    
    if val == root.key:

        if root is not None:

            result.append(root.key)

        if root.left is not None:

            result.append(root.left.key)

        if root.right is not None:

            result.append(root.right.key)      

        return result     
    
    if val < root.key:

        return findVal(root.left, val)

    if val > root.key:

        return findVal(root.right, val)

    return False