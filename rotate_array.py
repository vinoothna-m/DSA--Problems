"""rotate array -shifting elements(right rotation by k-steps)
"""

def rotate_array(arr,k):
    n=len(arr)
    k=k%n #normalize k
    def reverse(subarr,left,right):
        while left<right:
            subarr[left],subarr[right]=subarr[right],subarr[left]
            left+=1
            right-=1
#reverse whole array
    reverse(arr,0,n-1)
#reverse first k elements
    reverse(arr,0,k-1)
#reverse remaining n-k elements(reverse trick for efficiency)
    reverse(arr,k,n-1)
    return arr

#example
print(rotate_array([1,2,3,4,5,6],4))


"""Complexity analysis:
Time complexity: O(n)
Space complexity: O(1)"""
