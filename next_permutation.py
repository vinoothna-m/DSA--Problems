def next_permutation(arr):
    n=len(arr)
    pivot=-1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break
    if pivot==-1:
        arr.reverse()
        return
    for i in range(n-1,pivot,-1):
        if arr[i]>arr[pivot]:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            break
    left,right=pivot+1,n-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

#Example usage
arr=[2,4,1,7,5,0]
print(next_permutation(arr))

"""Time complexity=O(n)
Space complexity=O(1)"""
