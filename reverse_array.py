#reverse an array using slicing
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

#using swapping - time and space complexities=O(n),O(1)
arr=[1,2,3,4,5,6]
i=0
n=len(arr)
mid=n//2
while i<mid:
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    i+=1
print(arr)


