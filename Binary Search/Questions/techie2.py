# Search an element in a circularly sorted array

# Given a circularly sorted integer array, search an element in it. 
# Assume there are no duplicates in the array, and the rotation is in the anti-clockwise direction.

# 1. State the problem clearly and state sample inputs and outputs
    # Sample inputs and output

    #inputs : 
        # nums = [8, 9, 10, 2, 5, 6]
        # target = 10

    # output :
        # output : 2     

# 2. Test Case Examples
tests = []

# Case 1: Target is at left side possition

tests.append(
    {
        'inputs': {
            'nums': [8, 9, 10, 2, 5, 6],
            'target': 10
        },
        'output': 2
    }
)

# Case 2: Target is at right side possition

tests.append(
    {
        'inputs': {
            'nums': [8, 9, 10, 2, 5, 6],
            'target': 5
        },
        'output': 4
    }
)

# Case 3: Target is not present

tests.append(
    {
        'inputs': {
            'nums': [8, 9, 10, 2, 5, 6],
            'target': 1
        },
        'output': -1
    }
)

# Case 4: nums is empty

tests.append(
    {
        'inputs': {
            'nums': [],
            'target': 1
        },
        'output': -1
    }
)
