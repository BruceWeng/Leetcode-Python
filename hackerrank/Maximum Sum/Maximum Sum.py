'''
1. Build a main function to parse data to:
    1. n: number of integers
    2. t: target number
    3. nums: integer array
2. Handle edge cases: if n == 0 or t == 0: return 0
3. Declare two pointers 'start' = 0 and 'end' = 0 to trace the valid consecutive numbers interval
4. Declare variables 'result' = 0 for maximum sum and 'total'= 0 for local sum while iterate the nums
5. While end pointer < length n:
        1. while end pointer < n and total < t:
            Still have place to increment total
            1. assign max(result, total) to result
            2. total += nums[end]
            3. increment end pointer
        2. if total == t:
            return total
        3. while start <= end and total > t:
            need to decrement total to meet requirement
            1. total -= nums[start]
            2. increment start pointer
        4. assign max(result, total) to result
6. return result

Because we are not using extra data structures and only move pointers through the array for one time.
Time Complexity: O(n)
Space Complexity: O(1) (if we count the space building nums array then O(n))

This is the most efficient solution I can think of.
'''

def maxSum(n, nums, t):
    if n == 0 or t == 0:
        return 0

    start = 0
    end = 0
    result = 0
    total = 0
    while end < n:
        while end < n and total < t:
            result = max(result, total)
            total += nums[end]
            end += 1

        if total == t:
            return total

        while start <= end and total > t:
            total -= nums[start]
            start += 1

        result = max(result, total)
    return result


def main():
    data = raw_input().split(' ')
    n = int(data[0])
    t = int(data[1])
    nums = map(int, raw_input().split(' '))
    print maxSum(n, nums, t)

if __name__ == '__main__':
    main()
