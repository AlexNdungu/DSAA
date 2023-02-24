class TreeNode:

    def __init__(self, key):
        
        self.key = key
        self.right = None
        self.left = None


#Create a tuple representing the keys
tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))    

#Fuction that automates tree creation
def parse_tuple(data):

    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:

        node = None

    else:

        node = TreeNode(data)

    return node      


#Now pass the tuple 

tree = parse_tuple(tree_tuple) 

print(tree.left.key)