"""anagram- check two strings if they have same chars in any order
if length differs-not anagrams
count frequency of each char in first string
subtract frequency usign chars from second string
if all counts return to zero-they are anagrams
"""

def anagrams(s1,s2):#def anagrams(s1:str,s2:str)->bool:
    if len(s1)!=len(s2):
        return False
    char_count={}
    for ch in s1:
        char_count[ch]=char_count.get(ch,0)+1
    for ch in s2:
        if ch not in char_count or char_count[ch]==0:
            return False
        char_count[ch]-=1
    return True

#example
print(anagrams("listen","silent"))
print(anagrams("hello","world"))

"""Complexity analysis:
Time complexity: O(n)
Space complexity: O(1)"""
