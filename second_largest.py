#find second largest element in an array
#it performs better - time and space complexities=O(n),O(1)
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



#another method
def second_largest(arr):
    arr=list(set(arr))
    arr.sort()
    if len(arr)>1:
        return arr[-2]
    return -1
arr=[5,12,7,3,1,19]
print(second_largest(arr))

