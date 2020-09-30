# Question : https://leetcode.com/problems/largest-time-for-given-digits/ 
# Author : Samir Rajesh Prajapati
# Date : 1st October, 2020

# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. 
# The earliest 24-hour time is 00:00, and the latest is 23:59.

# Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.

import itertools as it

class Solution:
    def largestTimeFromDigits(self, arr) -> str:
        arr = sorted(arr)[::-1]
        l = it.permutations(arr)
        
        for t in l:
            a, b, c, d = t
            hh = a * 10 + b
            mm = c * 10 + d
            
            if hh < 24 and mm < 60:
                return "%d%d:%d%d"%t
        return ""

if __name__ == '__main__':
    A = Solution()
    print(A.largestTimeFromDigits([1,2,3,4]))