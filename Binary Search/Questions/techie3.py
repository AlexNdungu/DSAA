# Find the first or last occurrence of a given number in a sorted array

# Given a sorted integer array, 
# find the index of a given number’s first or last occurrence. 
# If the element is not present in the array, report that as well.

# 1. State the problem crealy and give sample inputs and outputs

    # input:
        # nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
        #target = 5
    # output : 
        # first : 1
        # last : 3

# Test cases
tests = []

# Case 1: The element is present

tests.append({
    'input':{
        'nums' : [2, 5, 5, 5, 6, 6, 8, 9, 9, 9],
        'target': 5
    },
    'output': {
        'first': 1,
        'last': 3
    }
})

#Case 2: Element is absent

tests.append({
    'input':{
        'nums' : [2, 5, 5, 5, 6, 6, 8, 9, 9, 9],
        'target': 4
    },
    'output': 'Element Not Present in nums'
})

# 3. State the solution in plain english (algorithim)
#O(log N) - Binary Search : 
    # 1. Find the most central index in nums
        # - Find the lowest (low) and the highest (high) index
        # - Add the two indexs the divide (//) by 2 to find the most central index (mid)
    # 2, if nums[mid] == target and target > nums[mid - 1], first = mid
    # 3, if nums[mid] == target and target < nums[mid + 1], last = mid
    # 4. if target < nums[mid], move left - high = mid - 1
    # 5. if target > nums[mid], move right - low = mid + 1
    # 6. if target == nums[mid] and target == nums[mid - 1] and target == nums[mid + 1] and first != Null, move right - low = mid + 1
    # 7. if target == nums[mid] and target == nums[mid - 1] and target == nums[mid + 1] and last != Null, move left - high = mid - 1

# 4. Implement the solution and debug the code

def findFirtsLast(nums, target):

    # The index of first and last position of element
    first = None
    last = None

    low = 0
    high = len(nums) - 1

    while low <= high:

        #print(high)

        if first == None or last == None:

            mid = (low + high) // 2 

            print(mid)

            #Start Conditions
            if nums[mid] == target: 
                
                if target > nums[mid - 1]:

                    # Record First index
                    first = mid

                    #print(first)
                    #print(last)

                if target < nums[mid + 1]:

                    # Record last element
                    last = mid

                    #print(last)
                    #print(first)

                if target >= nums[mid - 1] and target <= nums[mid + 1] and first != None: 

                    low = mid + 1   

                if target == nums[mid - 1] and target == nums[mid + 1] and last != None:

                    high = mid - 1


            if target < nums[mid]:

                # Move Left
                high = mid - 1

            if target > nums[mid]:

                # Move Right
                low = mid + 1  

        elif first != None and last != None:

            #print('last')

            #return print('The first occurrence of element {target} is located at index {first}'.format(target,first))#,'The Last occurrence of element {target} is located at index {last}'.format(target,last) 
            # 
            return last

    return 'Element not found in the array'        

#Lets test

test = {
    'input':{
        'nums' : [2, 5, 5, 5, 5 , 6, 6, 8, 9, 9, 9],
        'target': 5
    },
    'output': {
        'first': 1,
        'last': 3
    }
}

#print(findFirtsLast(test['input']['nums'],test['input']['target']))

# Finding first occurrence of the element

# def findFirstOccur(nums, target):

#     low = 0
#     high = len(nums) - 1

#     while low <= high:

#         mid = (low + high) // 2

#         #print(mid)

#         #The logic [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
#         if target == nums[mid]:
            
#             if target > nums[mid - 1]:

#                 return mid

#             if target == nums[mid + 1]:

#                 high = mid - 1

#         if target < nums[mid]:

#             high = mid - 1

#         if target > nums[mid]:  

#             low = mid + 1 

#     return 'none'   


# print(findFirstOccur(test['input']['nums'],test['input']['target']))    

def findLastOccure(nums, target):

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = (low + high) // 2

        print(mid)

        #The logic [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
        if target == nums[mid]:
            
            if target < nums[mid + 1]:

                return mid

            if target == nums[mid - 1] or target > nums[mid - 1]:

                low = mid + 1

        if target < nums[mid]:

            high = mid - 1

        if target > nums[mid]:  

            low = mid + 1 

    return 'none'   

print(findLastOccure(test['input']['nums'],test['input']['target']))