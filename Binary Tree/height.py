# Getting the height of the tree

def tree_height(node):

    if node is None:

        return 0
    
    return 1 + max(tree_height(node.left), tree_height(node.right))


# Lets find the number of elements in the tree

def tree_size(node):

    if node is None:

        return 0
    
    return 1 + tree_size(node.left) + tree_size(node.right)