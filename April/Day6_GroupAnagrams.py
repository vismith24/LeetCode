'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for string in strs:
            count = [0] * 26
            
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            ans[tuple(count)].append(string)

        return ans.values()