"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
"""
Algorithm 1:
0: The max profit on ith day with k transaction is
max(not transaction on ith day or transaction on ith day)
= max(same profit on i-1th day with k transaction or profit between ith day(sell)
and jth day(buy) + profit on j-1th day(if we buy stock on jth day, profit on jth
day is the same as j-1th day) with k-1 transaction)
1: dp[k][i] = max(dp[k][i-1], prices[i] - prices[j] + dp[k-1][j-1])
2. Declare a int dp[k][n] stores max profit for k transactions on ith day
3. Since we only allow two transactions, iterate from k = 1, k <= 2
4. Iterate the prices and find the max profit from jth to ith day aka. find min
value of minVal(initialed as prices[0]) and prices[j] - dp[k-1][j-1]
5. dp[k][i] = max(dp[k][i-1], prices[i] - minVal)
6. return dp[2][n-1]

T: O(kn^2)
S: O(kn)

Algorithm 2: See https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
how to optimize the solution to
T: O(kn)
S: O(k)
"""
def maxProfitDP(prices):
    if prices == None or len(prices) == 0:
        return 0

    n = len(prices)
    dp = [[0 for j in range(n)] for i in range(3)]
    for k in range(1, 3):
        for i in range(n):
            minVal = prices[0]
            for j in range(1, i+1):
                minVal = min(minVal, prices[j] - dp[k-1][j-1])
            dp[k][i] = max(dp[k][i-1], prices[i] - minVal)
    return dp[2][n-1]

import sys
def maxProfitDPOptimized(prices):
    buy1 = sys.maxsize
    buy2 = sys.maxsize
    sell1 = 0
    sell2 = 0

    n = len(prices)
    for i in range(n):
        buy1 = min(buy1, prices[i])
        sell1 = max(sell1, prices[i] - buy1)
        buy2 = min(buy2, prices[i] - sell1)
        sell2 = max(sell2, prices[i] - buy2)

    return sell2
