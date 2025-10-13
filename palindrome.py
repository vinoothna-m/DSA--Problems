"""palindrome-reads same forwards and backwards
use two pointers-one at start,one at end
compare chars:  if mismatch-return false
                move pointers inward until they meet
if all chars match-return true
"""


def is_palindrome(s):#def is_palindrome(s:str)->bool:
    left,right=0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

#example
print(is_palindrome("madam"))
print(is_palindrome("hello"))

"""Complexity analysis:
Time complexity: O(n)
Space complexity: O(1)"""
