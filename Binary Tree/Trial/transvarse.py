# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# left > root > right

def inorderTransversal(root):

    if root is None:
        return []
    
    return (inorderTransversal(root.left) + [root.key] + inorderTransversal(root.right))


#preorder

# root > left > right

def preorderTransversal(root):

    if root is None:
        return []
    
    return ([root.key] + preorderTransversal(root.left) + preorderTransversal(root.right))


# post order transerversal

# left > right > root

def postorderTransversal(root):

    if root is None:
        return []
    
    return (postorderTransversal(root.left) + postorderTransversal(root.right) + [root.key])
