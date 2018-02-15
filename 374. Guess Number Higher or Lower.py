"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
"""
"""
Algorithm: Binary Search
"""
"""
@param {int} n
@return {int}
"""
def guessNumber(n):
    if n <= 0: return -1

    start = 1
    end = n

    while start + 1 < end:
        mid = start + (end - start) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            end = mid
        else:
            start = mid

    return start if guess(start) == 0 else end
