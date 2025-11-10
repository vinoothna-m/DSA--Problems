#find second largest element in an array
#it performs better - time and space complexities=O(n),O(1)

def getSecondLargest(arr):
    n=len(arr)
    if n<2:
        return -1
    first=second=float('-inf')
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    if second==float('-inf'):
        return -1
    else:
        return second
arr = [12, 35, 1, 10, 34, 1]
print(getSecondLargest(arr))    



#better approach 
arr=[5,12,7,3,1,19]
largest=second_largest=float('-inf')
for n in arr:
    if n>largest:
        second_largest=largest
        largest=n
    if n>second_largest and n!=largest:
        second_largest=n
if second_largest==float('-inf'):
    print("no second largest element")
else:
    print(second_largest)


# Python program to find the second largest element in the array
# using two traversals
def getSecondLargest(arr):
    n = len(arr)

    largest = -1
    secondLargest = -1

    # Finding the largest element
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    # Finding the second largest element
    for i in range(n):
        
        # Update second largest if the current element is greater
        # than second largest and not equal to the largest
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
    
    return secondLargest

arr = [12, 35, 1, 10, 34, 1]
print(getSecondLargest(arr))



