"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as
you like (ie, buy one and sell one share of the stock multiple times) with the following
restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock
before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
"""
Algorithm:
1. In each day, there are three possible actions: buy, sell or cooldown
2. Define transfer functions:
    a. buy[i]: before ith day, last day action is "buy", maxProfit
    b. sell[i]: before ith day, last day action is "sell", maxProfit
    c. cooldown[i]: before ith day, last day action is "cooldown", maxProfit
3. Therefore transfer functions are:
    a. buy[i] = max(buy on ith day, not buy on ith day) = max(cooldown[i - 1] - price, buy[i - 1])
    b. sell[i] = max(sell on ith day, not sell on ith day) = max(buy[i - 1] + price, sell[i - 1])
    c. cooldown[i] = max(buy[i - 1], sell[i - 1], cooldown[i - 1])
4. To prevent [buy, cooldown, buy] condition: buy[i] < cooldown[i]
5. The day before cooldown day must be sell day: cooldown[i] = sell[i - 1]
6. New Transfer functions:
    buy[i] = max(sell[i - 2] - price, buy[i - 1])
    sell[i] = max(buy[i - 1] + price, sell[i - 1])
7. Since i only depends on i - 1 and i - 2, optimize space with rolling array:
    buy = max(previous_sell - price, previous_buy)
    sell = max(previous_buy + price, previous_sell)
"""
"""
@param {int[]} prices
@return {int}
"""
def maxProfit(prices):
    if len(prices) < 2:
        return 0
    buy = [None] * len(prices)
    sell = [None] * len(prices)
    buy[0] = -prices[0]
    buy[1] = max(-prices[0], -prices[1])
    sell[0] = 0
    sell[1] = max(prices[1] - prices[0], 0)
    for i in range(2, len(prices)):
        buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
        sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
    return sell[len(prices) - 1]

if __name__=="__main__":
    print(maxProfit([1, 2, 3, 0, 2])) # 3
