"""
@params {int[]} nums
@return {void}

Objective: Remove all zero to the back of the array

Assumption:
1. elements are all integers
2. ...

Algorithm:
input [1, 3, 6, 0, 1, 0, 2, 3]
insert          ^
input [1, 3, 6, 1, 1, 0, 2, 3]
insert             ^
input [1, 3, 6, 1, 2, 0, 2, 3]
insert                ^
input [1, 3, 6, 1, 2, 3, 2, 3]
insert                   ^
input [1, 3, 6, 0, 1, 0, 0, 0]
"""
