# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

def maxRoute(node):

    if node is None:#
        return 0
    
    return 1 + max(maxRoute(node.left),maxRoute(node.right))
