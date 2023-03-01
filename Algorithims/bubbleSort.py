# Write a fuction to sort nums in ascending order

#Test cases
#Test case 0:  List of numbers in random order

test0 = {
    'input':{
        'nums': [4,2,6,3,4,6,2,1]
    },
    'output': [1,2,3,3,4,4,6,6]
}

#Test case 1:  List of numbers in random order

test1 = {
    'input':{
        'nums': [5,2,6,1,23,7,-12,12,-234,0]
    },
    'output': [-243,-12,0,1,2,5,6,7,12,23]
}


#Test case 2:  List of numbers already sorted

test2 = {
    'input':{
        'nums': [1,2,3,3,4,4,6,6]
    },
    'output': [1,2,3,3,4,4,6,6]
}


#Test case 3:  List of numbers sorted in descending order

test3 = {
    'input':{
        'nums': [99,10,9,8,6,5,3]
    },
    'output': [3,5,6,8,9,10,99]
}


#Test case 4:  List with repeating numbers

test4 = {
    'input':{
        'nums': [5,-12,2,6,1,23,7,7,-12,6,12,1,-243,1,0]
    },
    'output': [-243,-12,-12,0,1,1,1,2,5,6,6,7,7,12,23]
}

#Test case 5:  Empty list

test5 = {
    'input':{
        'nums': []
    },
    'output': []
}

# Test case 6: A really long list

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test6 = {
    'input':{
        'nums': in_list
    },
    'output': out_list
}


# Add the list of tests to a new list

tests = [test0,test1,test2,test3,test4,test5,test6]



def bubbleSort(nums):
    
    # Create a copy of the list for the purpose of the test cases
    nums = list(nums)

    for _ in range(len(nums - 1)):

        for i in range(len(nums - 1)):

            if nums[i] > nums[i + 1]:

                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums                                                                                                                                                                                                       