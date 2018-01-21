"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Note: This solution exceed time limit in large number
"""
"""
@params {int} n
@return {int}
"""
def countPrimes(n):
    if n == 0 or n == 1:
        return 0
    # 1. Initiate isPrime array with all Trues
    # 2. Start i from 2 to n ** 0.5, label its multiples to False
    # 3. Count numbers of True in isPrime
    isPrime = [True] * (n - 1) # index: 0 -> n-1, value: 1 -> n
    isPrime[0] = False
    for i in range(2, int(n ** 0.5) + 1):
        end = int((n - 1) / i) + 1
        # Skip itself, j starts from 2
        for j in range(2, end):
            if isPrime[i * j - 1] == True:
                isPrime[i * j - 1] = False

    count = 0
    for flag in isPrime:
        if flag == True:
            count += 1
    return count

if __name__=="__main__":
    test1 = 10
    print(countPrimes(test1)) # 4
    test2 = 120
    print(countPrimes(test2)) # 30
