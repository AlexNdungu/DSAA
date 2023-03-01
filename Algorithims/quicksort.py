# Quick sort algorithim

def quickSort(nums, start = 0, end=None):
    
    if end is None:

        nums = list(nums)
        end = len(nums) - 1

    if start < end:

        pivot = partition(nums,start,end)
        quickSort(nums, start, pivot - 1)
        quickSort(nums, pivot + 1, end)

    return nums    