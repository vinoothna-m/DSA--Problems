#find minimum and maximum values in an array
"""take an array as input
swap first and last elements then move inward until middle
this reverses must takes in-place"""

def reverse_array(arr):
    left,right=0,len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right+=1
    return arr
print(reverse_array([1,2,3,4,5]))

arr=[5,12,7,3,1,19]
min=max=arr[0]
for n in arr:
    if n<min: min=n
    if n>max: max=n
print("minimum element:", min)
print("maximum element:", max)


#using in-built methods in python
arr=[5,12,7,3,1,19]
print(min(arr))
print(max(arr))


#in function form
def min_e(arr):
    return min(arr)
print(min_e(arr))
def max_e(arr):
    return max(arr)
print(max_e(arr))
arr=[5,12,7,3,1,19]

"""Complexity Analysis:
Time Complexity: O(n)
Space Complexity: O(1)"""
