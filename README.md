# Data Structures And Algorithims

## Leason One - Binary Search, Linked List And Complexity

___

- Understand the question asked by the interviewer
- Define and outline test cases
- Define an algorithim to effectively carry out the search
- Write the code and debug any error
- Big O notation

___
![Binary Search VS Linear Search](https://www.codesdope.com/staticroot/images/algorithm/binary_search.gif)

### Generic Binary Search Fuctions

```
 #Binary search fuction that can be used everywhere
def binary_search(lo,hi, condition):

    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def locate_cards(cards, query):

    def condition(mid):

        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)                        
```

___

## Leason Two - Binary Search Ree, Transversal And Balancing

### Write a Python program to create a Balanced Binary Search Tree (BST) using an array of elements where array elements are sorted in ascending order.

___

#### &rarr; array = [1, 2, 3, 4, 5, 6, 7]

### The Code &darr;

```
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
result = createTree(the_array)

# Now lets display the tree

def preOrder(node):

    if not node:
        return None
    print(node.key)
    preOrder(node.left)    
    preOrder(node.right)

preOrder(result)

```

![Binary Search Tree](https://www.w3resource.com/w3r_images/python-binary-search-tree-image-exercise-1.svg)

## Traversing A Tree

&rarr; Process of visiting each tree node only once.

- inorder
- preorder
- postorder

![Binary Search Tree Traversal](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Preorder-from-Inorder-and-Postorder-traversals.jpg)

## Key- Value Pair Trees

&rarr; The node contains a key and a value

```
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

```
