'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar, maxEndingHere = -sys.maxsize - 1, 0
        
        for i in range(len(nums)):
            maxEndingHere += nums[i]
            
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
                
            if maxEndingHere < 0:
                maxEndingHere = 0
        
        return maxSoFar
        
