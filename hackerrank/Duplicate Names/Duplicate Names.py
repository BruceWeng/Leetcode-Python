'''
Given a list of N patient records, you have to determine the unique records by eliminating the duplicates.

Input format:
The first line contains an integer N, N lines follw each line having:
NAME:SSN
A NAME can be in any of the following forms:
1. <First Name>
2. <Last Name>,<First Name>
3. <First Name> <Last Name>
4. <Last Name>,<First Name> <Middle Name>
5. <First Name> <Middle Name> <Last Name>
6. <First Initial>.<Middle Inital>.<Last Name>
7. <FIrst Name> <Middle Inital>.<Last Name>

The order for the multiple forms of the name Maggie Fitzgerald Fergusson is

Maggie < Maggie Fergusson < M. F. Fergusson < Maggie F.Fergusson < Maggie Fitzgerald Fergusson

Sample Input:
9
MERVIN:865965036
BOUCK,MERVIN:865965036
MERVIN BOUCK:865965036
BOUCK,MERVIN ADELINE:865965036
MERVIN ADELINE BOUCK:865965036
LEN:992989227
GERALD:358648156
BYER,GERALD:358648156
GERALD BYER:358648156

Sample Output:
MERVIN ADELINE BOUCK:865965036
LEN:992989227
GERALD BYER:358648156

Explanation:
There are 3 SSNs. 865965036, 992989227, 358648156
and the correct name for each SSN with the highest order is MERVIN AEDLINE BOUCK, LEN and GERALD BYER respectively.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    n = int(raw_input())
    for i in xrange(n):
        patient = input().split(':')

    print n
    print patient
if __name__ == '__main__':
    main()
