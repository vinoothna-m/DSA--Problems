#find minimum and maximum values in an array
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

