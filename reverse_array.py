#REVERSE AN ARRAY
"""take two pointers left at beginning and right at end of array
swap first and last elements when left < right
increment left and decrement right until reaches the two pointers to middle
this reverses must takes in-place"""
#optimal approach- using two pointers

def reverse_array(arr):
    left,right=0,len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right+=1
    return arr
print(reverse_array([1,2,3,4,5]))

"""Complexity Analysis:
Time Complexity: O(n)
Space Complexity: O(1)"""

#using slicing
arr=[1,2,3,4,5,6]
rev=arr[::-1]
print(rev)

#using built-in method
arr=[1,2,3,4,5,6]
arr.reverse()
print(arr)

#using loop
arr=[1,2,3,4,5]
n=len(arr)
rev=[]
for i in range(n-1,-1,-1):
    rev.append(arr[i])
print(rev)

#using swapping
arr=[1,2,3,4,5,6]
i=0
n=len(arr)
mid=n//2
while i<mid:
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    i+=1
print(arr)




