def stockMax(n, prices):
    result = 0
    localMax = prices[n - 1]
    for i in range(n - 2, -1, -1):
        if prices[i] <= localMax:
            result += localMax - prices[i]
        else:
            localMax = prices[i]

    print result

def main():
    t = input()
    for i in range(t):
        n = input()
        prices = map(int,raw_input().split(' '))
        stockMax(n, prices)

if __name__ == '__main__':
    main()
