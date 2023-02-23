# Given an array nums sorted in non-decreasing order. (The next number in the array is greater or equal to the previous) [-4,-4,-3,-3,0,1,2,2]
# Return the maximum between the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, 
# then return the maximum of pos and neg.

# 1. State the statement problem cleary. Give exmaples of inputs and outputs
    # - Transverse through an array () arranged in a non-decreasing order. Count all the negative numbers(neg) and positive numebrs (pos).
    # - Compare then the count of pos and neg and return the largest number

    # Inputs :
    # nums = [-4,-4,-3,-3,0,1,2,2]

    # Output : (pos = 3, neg = 4) note: 0 is neither positive or negative = 4

# 2. Test Case Examples

tests = []

# Case 1: When negative and positive numbers are equal

tests.append({
    'input': {
        'nums': [-2,-1,-1,1,2,3]
    },
    'output': 3
})

# Case 2: When there are more negative numbers than the positive

tests.append({
    'input': {
        'nums': [-3,-2,-1,0,0,1,2]
    },
    'output': 3
})

# Case 3: When the positive numbers are more than the negative 

tests.append({
    'input': {
        'nums': [-3,-2,-1,0,0,1,1,2,3]
    },
    'output': 4
})

# Case 4: When nums is made up of only 0s

tests.append({
    'input': {
        'nums': [0,0,0,0]
    },
    'output': 0
})

# Case 5: When nums is madeup of only positive numbers

tests.append({
    'input': {
        'nums': [1,3,4,5,7,8]
    },
    'output': 6
})


# Case 6: When nums is made up of only negative numbers

tests.append({
    'input': {
        'nums': [-1,-3,-4,-5,-7,-8]
    },
    'output': 6
})


#