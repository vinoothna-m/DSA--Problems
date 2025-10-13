"""check if array is sorted
simply check if each element is less than or equal to next
"""
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:#array not sorted
            return False
    return True

#example
print(is_sorted([1,2,3,4,5]))
print(is_sorted([1,4,2,6]))

"""Complexity analysis:
Time complexity: O(n)
Space complexity: O(1)"""
