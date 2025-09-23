#Linear search
"""Traverse array first
check element equals to target-return index
if element not found-return -1
"""

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print(linear_search([1,3,4,3,5,6,7],8))

"""Complexity Analysis:
Time Complexity: O(n)
Space Complexity: O(1)"""
