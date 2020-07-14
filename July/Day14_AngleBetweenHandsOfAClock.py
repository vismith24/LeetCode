'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:

Input: hour = 12, minutes = 30
Output: 165
'''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(30 * hour - 5.5 * minutes)
        
        return min(angle, 360 - angle)
        