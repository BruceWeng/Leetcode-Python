def subsequence(k, n, array):
    result = 0
    for i in range(n):
        for j in range(i+1, n+1):
            temp = [array[x] for x in range(i, j)]
            if sum(temp) % k == 0:
                result += 1
    print result

def main():
    t = input()
    for i in range(t):
        data = map(int, raw_input().split(' '))
        n = data[0]
        k = data[1]
        array = map(int, raw_input().split(' '))
        subsequence(k, n, array)
if __name__ == '__main__':
    main()
