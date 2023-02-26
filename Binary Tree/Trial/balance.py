# Check if the tree is balance
# left tree height and right tree height difference is not more than 1

def isBalanced(node):
    
    if node is None:

        return 0
    
    balance_value = isBalanced(node.right) - isBalanced(node.left)

    if balance_value <= 1:

        return True
    
    else:

        return False
    #return 1 + min(isBalanced(node.right),isBalanced(node.left))
