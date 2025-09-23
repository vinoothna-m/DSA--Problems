#Move zeros
#shift all non zero elements to left,must done in-place
"""non zero index keeps track of where to put next non zero elements
traverse array-if element is non zero place it at that index
after traversal fill remaining slots with zero"""

def move_zeros(arr):
    non_zero_index=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[non_zero_index],arr[i]=arr[i],arr[non_zero_index]
            non_zero_index+=1
    return arr
arr=[0,1,0,3,12]
print(move_zeros(arr))



"""Complexity Analysis:
Time Complexity: O(n)
Space Complexity: O(1)"""
