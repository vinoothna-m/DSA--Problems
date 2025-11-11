#MOVE ZEROS TO END OF ARRAY
#shift all non zero elements to left,must done in-place
"""initialize count=0 which keeps track of where to put next non zero elements
traverse array-if element is non zero place it at that index
after traversal fill remaining slots with zero"""
#optimal approach - using one traversal

def move_zeros(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[count]=arr[count],arr[i]
            count+=1
    return arr
arr=[0,1,0,3,12]
print(move_zeros(arr))

"""Complexity Analysis:
Time Complexity: O(n)
Space Complexity: O(1)"""


