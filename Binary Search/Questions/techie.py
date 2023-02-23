# Given a circularly sorted integer array, [4, 5, 6, 7, 1, 2, 3]
# find the total number of times the array is rotated. 
# Assume there are no duplicates in the array, and the rotation is in the anti-clockwise direction.

# 1. State The problem clearly . Identify inputs and output formats
    # - Find the number of elements that have been rotated to find how many times the array has been rotated

    # Input : [4, 5, 6, 7, 1, 2, 3]
    # Output : 4
    # Array ahs been rotated 4 times

# 2. Test Cases    
tests = []

# Case 1: No Rotations

tests.append({
    'input' :{
        'nums' : [2, 5, 6, 8, 9, 10]
    },
    'output': 0
})
    
# Case 2: Rotated completely

tests.append({
    'input' :{
        'nums' : [10,9,8,6,5,2]
    },
    'output': 6
})

# Case 3: Rotated N number of times

tests.append({
    'input' :{
        'nums' : [8 ,9 ,10 , 2, 5, 6]
    },
    'output': 3
})

# 3. State the solution in plain english
#O(log N) - Binary Search : 
    # 1. Find the most central index in nums
        # - Find the lowest and the highest index
        # - Add the two indexs the divide (//) by 2 to find the most central index
    # 2. if nums[mid - 1] > nums[mid], 