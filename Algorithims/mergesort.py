# Lets implement the merge sort algorthim

#Helper fuction

def merge(left_list,right_list):

    complete_sorting = []

    #indices for iteration
    i,j = 0,0

    while i < len(left_list) and j < len(right_list):

        # include the smaller element in the result and move to next element
        if left_list[i] <= right_list[j]:
            complete_sorting.append(left_list[i])
            i += 1

        elif right_list[j] <= left_list[i]:
            complete_sorting.append(right_list[j])
            j += 1

    #After exhausting one list
    left_list_tail = left_list[i:]
    right_list_tail = right_list[j:]


    return complete_sorting + left_list_tail + right_list_tail    



def mergeSort(nums):

    if len(nums) <= 1:
        return nums
    
    #Get mid point
    mid = len(nums) // 2

    #Split the list into 2 halves
    left = nums[:mid]
    right = nums[mid:]

    #Solve the problem for each side recursivly
    left_sorted, right_sorted = mergeSort(left), mergeSort(right)

    sorted_numbers = merge(left_sorted, right_sorted)

    return sorted_numbers


# Now lets test
#Test cases
#Test case 0:  List of numbers in random order

test0 = {
    'input':{
        'nums': [4,2,6,3,4,6,2,1]
    },
    'output': [1,2,2,3,4,4,6,6]
}

#Test case 1:  List of numbers in random order

test1 = {
    'input':{
        'nums': [5,2,6,1,23,7,-12,12,-234,0]
    },
    'output': [-234,-12,0,1,2,5,6,7,12,23]
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

#Now lets test

from jovian.pythondsa import evaluate_test_cases,evaluate_test_case

evaluate_test_cases(mergeSort, tests)

#mergeSort(test0['input']['nums'])
