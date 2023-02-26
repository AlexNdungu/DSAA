# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

def maxRoute(node):

    if node is None:#
        return 0
    
    return 1 + max(maxRoute(node.left),maxRoute(node.right))


def minRoute(node):
    

    if node is None:#
        return 0
    
    if node.left is None:
        return minRoute(node.right) + 1

    if node.right is None:
         return minRoute(node.left) + 1
    
    return 1 + min(minRoute(node.left),minRoute(node.right))


#Get the max and inimum value in 