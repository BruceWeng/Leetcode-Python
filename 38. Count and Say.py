"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

Example of nth sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
 10.    13211311123113112211
"""
"""
Algorithm:
1. Declare an inner helper function receive string and return next string
2. Helper function:
    a. declare result as an empty string
    b. add "#" in the end of string as a stop point
    c. initial count = 1
    d. iterate string, if there is duplicate(string[i] == string[i+1]):
         count += 1
         continue
       else: (no duplicates)
         result += str(count) + string[i]
         count = 1 (reset count)
    e. return result
3. starting from "1", update the start from 0 to n-1 
"""
def countAndSay(n):
    if n <= 0:
        return ""

    # Convert to a question with input string "1"
    def helper(string):
        result = ""
        string += "#"
        count = 1

        for i in range(len(string) - 1):
            if string[i] == string[i+1]:
                count += 1
                continue
            else:
                result += str(count) + string[i]
                count = 1
        return result

    start = "1"
    for i in range(n - 1):
        start = helper(start)
    return start
