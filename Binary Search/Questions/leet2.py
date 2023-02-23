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

# Case 7: When the firts element is 0

tests.append({
    'input': {
        'nums': [0,1,2,3,6,8]
    },
    'output': 5
})

# Case 8: When the last element is 0

tests.append({
    'input': {
        'nums': [-4,-3,-1,0,0]
    },
    'output': 3
})


# 3. State the solution in plain english (algorithim)
#O(log N) - Binary Search : 
    # 1. Find the most central index in nums
        # - Find the lowest (low_index) and the highest (high_index) index
        # - Add the two indexs the divide (//) by 2 to find the most central index (mid_index)
    # 2. If the value of nums[mid_index] is positive, check the left number - nums[mid_index - 1].
        # If the nums[mid_index - 1] is positive - move to the left and repeat 1
        # Else if nums[mid_index - 1] is negative - find its index and count the number of numbers from index 0 to the index [mid_index - 1]
        # Else if nums[mid_index - 1] = 0, move to the left and repeat 1
    # 3. Else if the value of nums[mid_index] is negative, check the number on the right - nums[mid_index + 1]
        # If nums[mid_index + 1] is negative, move to the right and repeat 1
        # Else if the number is positive, count the numer of elements between (nums[mid_index] - 0 = neg) and (high_index - nums[mid_index] = pos)
        # Else if the number is 0, move to the right and repeat 1


# 4. Implement the solution and debug the code

# def binary_position(low_index,high_index,condition):

#     while low_index <= high_index:

#         # Here we find the mid_index
#         mid_index = (low_index + high_index) // 2

#         result = condition(mid_index)

#         print(result)

#         if result == 'left':

#             high_index = mid_index - 1

#         elif result == 'right':

#             low_index = mid_index + 1

#         elif result == 'mid_positive':

#             print('middle of neg and pos')

#             #Lets count the positive values first [-4,-3,-2,1,2,3,3]
#             pos = (high_index - mid_index) + 1

#             #Lets count the negative values
#             neg = ((mid_index - 1) - low_index) + 1

#             #Now check the biggest value

#             if pos > neg:

#                 return pos

#             elif neg > pos:

#                 return neg

#         elif result == 'mid_negative': #[-4,-3,-2,-1,1,2,3]

#             #Lets first count the negative values
#             neg = (mid_index - low_index) + 1

#             #lets count the positive numbers
#             pos = (high_index - (mid_index + 1)) + 1

#             if pos > neg:

#                 return pos

#             elif neg > pos:

#                 return neg

#     return 0


# def count_nums(nums):

#     def condition(mid_index):

#         if nums[mid_index] > 0:

#             if nums[mid_index - 1] > 0:

#                 return 'left'

#             elif nums[mid_index - 1] < 0:

#                 return 'mid_positive' #One step to the left is a negative value

#             elif nums[mid_index - 1] == 0:

#                 return 'left'

#         elif nums[mid_index] < 0:

#             if nums[mid_index + 1] < 0:

#                 return 'right'

#             elif nums[mid_index + 1] > 0:

#                 return 'mid_negative' # One step to the right is a positive value

#             elif nums[mid_index + 1] == 0:

#                 return 'right'  

#     binary_position(0, len(nums) - 1, condition)   


# #Test one
# test = {
#     'input': {
#         'nums': [-1,-3,-4,-5,-7,-8]
#     },
#     'output': 6
# }

# print(count_nums(test['input']['nums']))
# #Now lets test t
# #from jovian.pythondsa import evaluate_test_cases

# #evaluate_test_cases(count_nums, tests)


#Correction

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive=0
        negative=0
        for i in nums:
            if i>0:
                positive+=1
            elif i<0:
                negative+=1
        return max(positive,negative)