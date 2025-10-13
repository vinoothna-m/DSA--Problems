"""reverse chars of a string
convert string -list(python strings are immutable)
swap chars from both ends until middle
join list back into a string"""


def rev_str(s):#def rev_str(s:str)->str:
    s=list(s)
    left,right=0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return "".join(s)

#example
print(rev_str("hello"))


"""Complexity analysis:
Time complexity: O(n)
Space complexity: O(n)"""
