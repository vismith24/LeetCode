'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subs = []
        
        for i in range(2 ** n, 2 ** (n + 1)):
            mask = bin(i)[3:]
            
            subs.append([nums[j] for j in range(n) if mask[j] == '1'])
        
        return subs