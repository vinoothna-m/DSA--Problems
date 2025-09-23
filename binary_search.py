#Binary search
"""It only works on sorted array
set low and high values
find mid and compare the low and high using target value
return index if found otherwise return -1
keep dividing array into half until target is found
"""

def binary_search(arr,x):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,3,5,7,12,19]
print(binary_search(arr,7))

"""Complexity Analysis:
Time Complexity: O(log n)
Space Complexity: O(1)"""
