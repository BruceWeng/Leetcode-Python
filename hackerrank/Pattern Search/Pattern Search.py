# Pattern Search

'''
You are provided a string S of length N. The only characters contained in it are the capital letters 'A', 'B', 'C', 'D'.
You are given a pattern P of length M. This pattrn is also composed of the uppercase letters 'A', 'B', 'C', 'D. However, it can also contains wildcard characters ('*').
Assuming that the wildcard character ould correspond to any of the 4 letters ('A' to 'D'), how many times does this pattern occur in the string S?

Input:
The first line contains two integers N and M seperated by spaces
The second line contains the String S.
The third line contains the String P.

Sample Input:
20 4
ABCDDDDABCDABCDDCCCB
AB*D

Sample Output:
3

Explanation:
Given, that the wildcard can match any of the 4 characters, these are the three groups where the match could occur.
(ABCD)DDD(ABCD)(ABCD)DCCCB

Available Language:
Python2
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def patternSearch(s, p):
    i = 0 # for pattern
    j = 0 # for string
    count = 0

    while i < len(p) and j < len(s):
        if i == len(p) - 1:
            count += 1
            i = 0

        if p[i] == '*':
            i += 1
            j += 1
        elif p[i] != s[j]:
            j += 1
        elif p[i] == s[j]:
            i += 1
            j += 1


    print count

def main():
    number = raw_input().split(' ')
    n = int(number[0])
    m = int(number[1])
    s = raw_input()
    p = raw_input()
    patternSearch(s, p)

if __name__ == '__main__':
    main()
