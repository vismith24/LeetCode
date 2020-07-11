'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

 

Note: You may assume the string contains only lowercase English letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
            
        for char in s:
            if hashMap[char] == 1:
                return s.index(char)
            
        return -1
        