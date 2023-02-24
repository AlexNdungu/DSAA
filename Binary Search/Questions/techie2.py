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
        'input': {
            'nums': [8, 9, 10, 2, 5, 6],
            'target': 10
        },
        'output': 2
    }
)

# Case 2: Target is at right side possition

tests.append(
    {
        'input': {
            'nums': [8, 9, 10, 2, 5, 6],
            'target': 5
        },
        'output': 4
    }
)

# Case 3: Target is not present

tests.append(
    {
        'input': {
            'nums': [8, 9, 10, 2, 5, 6],
            'target': 1
        },
        'output': -1
    }
)

# Case 4: nums is empty

tests.append(
    {
        'input': {
            'nums': [],
            'target': 1
        },
        'output': -1
    }
)


# 3. State the solution in plain english (algorithim)
#O(log N) - Binary Search : 
    # 1. Find the most central index in nums
        # - Find the lowest (low) and the highest (high) index
        # - Add the two indexs the divide (//) by 2 to find the most central index (mid)
    # 2. Check if target >= nums[low] and target >= nums[high], move left (high = mid - 1 )
    # 3. Check if target <= nums[low] and target <= nums[high], move right (low = mid + 1)
    # 4. if nums[mid] = targer - return mid, else error


# 4. Implement the solution and debug the code

def findTarget(nums, target):

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = (low + high) // 2

        #The checks
        # The mid is the target
        if nums[mid] == target:

            return mid

        #Check directions [8,9,10,2,5,6] - 5
        if  target >= nums[low] and target >= nums[high]:

            #Move left
            high = mid - 1

        elif target <= nums[low] and  target <= nums[high]:

            #Move right
            low = mid + 1

    return -1 #Invalid inout        


#Now lets test
test = {
        'input': {
            'nums': [8, 9, 10, 2, 5, 6],
            'target': 5
        },
        'output': 4
}

# {
#     'input': {
#         'nums': [10,12,13,24,36,47],
#         'target': 47
#     },
#     'output': 5
# }


#Now we test all the cases simultaniously
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

evaluate_test_cases(findTarget,tests)