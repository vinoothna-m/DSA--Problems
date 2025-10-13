"""fing missing number from 1 to n series
"""

def missing(arr):
    n=len(arr)
    expected_sum=(n+1)*(n+2)//2
    actual_sum=sum(arr)
    return expected_sum-actual_sum

#example
print(missing([1,2,3,5,6]))

"""Complexity analysis:
Time complexity: O(n)
Space complexity: O(1)"""
