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