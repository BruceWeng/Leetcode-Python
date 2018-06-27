"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Example 1:

Input: buf = "abc", n = 4
Output: "abc"
Explanation: The actual number of characters read is 3, which is "abc".
Example 2:

Input: buf = "abcde", n = 5
Output: "abcde"
Note:
The read function will only be called once for each test case.
"""
"""
Algorithm:
1. Declare index = 0
2. while index < n:
    2.a reinitial a new empty array [""] * 4
    2.b update count from read4()
    2.c if count == 0: break (EOF)
    2.4 updat count = min(count, n - index) (can not exceed max buffer length n)
    2.5 buf[i:] = buf4[:count]
    2.6 index += count
3. return index

T: O(n)
S: O(1)
"""
"""
@param {str[]} buf: Destination buffer
@param {int} n: Maximum number of characters to read
@return {int}: The number of characters read
"""
def read(buf, n):
    index = 0
    while index < n:
        buf4 = [" "] * 4
        count = read4(buf4)
        if count == 0:
            break

        count = min(count, n - index)
        buf[index:] = buf4[:count]
        index += count
    return index
