#LeetCode Question1

# Given an array of integers nums which is sorted in ascending order, and an integer target.
# write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity. (Divide And Concour : Binary Search)

#Constraints
# 1 <= nums.length <= 104
# -10^4 < nums[i], target < 104
#All the integers in nums are unique.
#nums is sorted in ascending order.

# 1. State The problem clearly . Identify inputs and output formats
    # - Transverse a sorted array(num2) and find the index of a specific item(target)

    # Inputs
    # nums = [1,3,5,7,8,12]
    # target = 5 

    # Expected Output
    # index = 2

# 2. Test Case Examples

#Case 1: The target is in the array

test = {
    'input': {
        'nums': [1,3,5,7,8,12],
        'target': 5
    },
    'output': 2
}

#Case 2: The target is not in the array

test = {
    'input': {
        'nums': [1,2,6,7,9,12],
        'target': 10
    },
    'output': -1
}

#Case 3: The target is the first element

test = {
    'input': {
        'nums': [10,12,23,44,46,67],
        'target': 10
    },
    'output': 0
}

#Test 4: The target is the last element

test = {
    'input': {
        'nums': [10,12,13,24,36,47],
        'target': 47
    },
    'output': 5
}

#Test 5: Only in element in nums

test = {
    'input': {
        'nums': [10],
        'target': 10
    },
    'output': 0
}
