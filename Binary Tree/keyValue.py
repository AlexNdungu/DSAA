# Soring key value pairs

class BSTNode():

    def __init__(self, key, value = None):

        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

#Create a fuction to insert nodes to tree

def insert(node, key, value):
    if node is None:
        node = BSTNode(key,value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


#Now let us find the value associated with a given key            

def find(node, key):

    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
    
# Now we update the values

def update(node, key, value):

    target = find(node, key)
    if target is not None:
        target.value = value

# Now list all the nodes in the tree (inorder traversal)

def all_list(node):

    if node is None:
        return []
    return all_list(node.left) + [(node.key,node.value)] + all_list(node.right)            


# Determining if a binary tree is balanced
# 1. Left subtree should be balanced
# 2. Right subtree should be balanced
# 3. Difference in heights of the left and right subtrees is <= 1

def is_balanced(node):

    if node is None:
        return True, 0
    
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_r,height_l)
    return balanced, height
