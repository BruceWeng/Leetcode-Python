"""
Convert a non-negative integer to its english words representation. Given input
is guaranteed to be less than 2^31 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
Thousand Eight Hundred Ninety One"
"""
"""
Algorithm:
1. Declare a hashSet lessThan20(str[]) to store words from "" to "Nineteen" (index: number, value: words)
   Declare a hashSet tens(str[]) to store words from "" to "Ninety" (index: number, value: words)
   Declare a hashSet thousands(str[]) to store words from "", "Thousand", "Million", to "Billion" (index: number, value: words)
2. Declare an empty queue result to store the English words
3. Write a helper function(num) to categorize the number into lessThan20, lessThan100 or others
    If num < 20: return lessThan20[num]
    elif num < 100: return tens[num/10] + helper(num/%10) <- key of the question
    else: return lessThan20[num/100] + "Hundred" + helper(num%100) <- key of the question
4. Iterate the range(len(thousands)):
        if num % 1000 != 0:
            result.appendleft(helper(num%1000) + thousands[i]))
            num /= 1000
5. Convert char array to a string
    " ".join(result)
6. Seperated by space whenever there is a uppercase
"""
"""
@param {int} num
@return {str} English words
"""
from collections import deque
def numberToWords(num):
    if num == None:
        return ""

    if num == 0:
        return "Zero"

    lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    thousands = ["","Thousand","Million","Billion"]

    """
    Convert number to words for numbers less than 1000
    @param {int} num
    @return {str}
    """
    def helper(num):
        if num == 0:
            return ""
        elif num < 20:
            return lessThan20[num]
        elif num < 100:
            return tens[num/10] + helper(num%10)
        else:
            return lessThan20[num/100] + "Hundred" + helper(num%100)

    result = deque([])

    for i in range(len(thousands)):
        if num % 1000 != 0:
            words = helper(num%1000) + thousands[i]
            result.appendleft(words)
        num /= 1000

    # Convert char array to a string
    result = "".join(result)
    # Seperated by space whenever there is a uppercase
    return "".join(" " + char if char.isupper() else char for char in result).strip()
