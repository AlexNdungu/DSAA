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

tests = []

#Case 1: The target is in the array

tests.append({
    'input': {
        'nums': [1,3,5,7,8,12],
        'target': 5
    },
    'output': 2
})

#Case 2: The target is not in the array

tests.append({
    'input': {
        'nums': [1,2,6,7,9,12],
        'target': 10
    },
    'output': -1
})

#Case 3: The target is the first element

tests.append({
    'input': {
        'nums': [10,12,23,44,46,67],
        'target': 10
    },
    'output': 0
})

#Test 4: The target is the last element

tests.append({
    'input': {
        'nums': [10,12,13,24,36,47],
        'target': 47
    },
    'output': 5
})

#Test 5: Only in element in nums

tests.append({
    'input': {
        'nums': [10],
        'target': 10
    },
    'output': 0
})


# 3. State the solution in plain english
#O(log N) - Binary Search : 
    # 1. Find the most central index in nums
        # - Find the lowest and the highest index
        # - Add the two indexs the divide (//) by 2 to find the most central index
    # 2. If the central most index is the matching target, stop the search else -
    # 3. Depending on the comparison of the ascending numbers, deside if to move on with the right side or the left side nums
    # 4. Repeat solution 2 and 3 until you find the target and display its index, else
    # 5. Return -1 (Target not found)

# 4. Implement the solution and debug the code


def find_target(high_index,low_index,target, nums):

    #Loop through the array
    while low_index <= high_index:

        mid_index = (high_index + low_index) // 2

        #Decide whether to go left or right
        #Considering that nums in sorted in ascending order [1,3,5,6,8,9,10] target = 3

        if target < nums[mid_index]:

            high_index = mid_index - 1

        elif target > nums[mid_index]:

            low_index = mid_index + 1

        elif target == nums[mid_index]:

            return nums[mid_index]

#Now we test unoptimized code
find_target()            
