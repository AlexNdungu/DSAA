# Lets implement the merge sort algorthim

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

        elif right_list[i] <= left_list[j]:
            complete_sorting.append(right_list[i])
            j += 1

    #After exhausting one list
    left_list_tail = left_list[i:]
    right_list_tail = right_list[j:]


    return complete_sorting + left_list_tail + right_list_tail    