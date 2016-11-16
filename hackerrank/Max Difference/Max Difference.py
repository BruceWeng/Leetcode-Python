def maxDiff(n, array):
    result = 0

    for i in range(n):
        for j in range(i+1, n+1):
            temp = sorted([array[x] for x in range(i, j)])
            minVal = temp[0]
            maxVal = temp[-1]
            result += maxVal - minVal
    print result

def main():
    n = input()
    array = map(int, raw_input().split(' '))
    maxDiff(n, array)

if __name__ == '__main__':
    main()
