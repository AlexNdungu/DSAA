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

___

## Leason Two - Binary Search Ree, Transversal And Balancing

### Write a Python program to create a Balanced Binary Search Tree (BST) using an array of elements where array elements are sorted in ascending order.

___

#### &rarr; array = [1, 2, 3, 4, 5, 6, 7]

### The Code &darr;

```
# Create The Tree class

class TreeNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Create a function that can divide this array and set the nodes

def createTree(nums):

    # Find the middle
    mid = len(nums) // 2

    if not nums:
        return None

    node = TreeNode(nums[mid])
    node.left = TreeNode(nums[:mid])
    node.right = TreeNode(nums[mid + 1:])
    return node

#Call the fuction
print(createTree(the_array))  

```

![Binary Search VS Linear Search](https://www.w3resource.com/w3r_images/python-binary-search-tree-image-exercise-1.svg)

