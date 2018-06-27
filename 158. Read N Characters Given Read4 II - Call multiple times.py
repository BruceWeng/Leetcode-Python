"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns
3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads
n characters from the file.

Note:
The read function may be called multiple times.

Example 1:

Given buf = "abc"
read("abc", 1) // returns "a" # Should return 1
read("abc", 2); // returns "bc" # Should return 2
read("abc", 1); // returns "" # Should return 0
Example 2:

Given buf = "abc"
read("abc", 4) // returns "abc" # Should return 3
read("abc", 1); // returns "" # Should return 0
"""
"""
Algorithm: Pointers
U1. se buffer pointer (buffPtr) and buffer Counter (buffCnt) to store the data
received in previous calls. In the while loop, if buffPtr reaches current buffCnt,
it will be set as zero to be ready to read new data.
"""

class Solution(object):
    def __init__(self):
        self.buff4Ptr = 0
        self.buff4Cnt = 0
        self.buff4 = [" "] * 4

    """
    @param {str[]} buf: Destination buffer
    @param {int} n: Maximum number of characters to read
    @return {str} The number of characters read
    """
    def read(self, buf, n):
        ptr = 0
        while ptr < n:
            if self.buff4Ptr == 0:
                self.buff4Cnt = read4(self.buff4)
            if self.buff4Cnt == 0:
                break
            while ptr < n and self.buff4Ptr < self.buff4Cnt:
                buf[ptr] = self.buff4[self.buff4Ptr]
                ptr += 1
                self.buff4Ptr += 1

            if self.buff4Ptr >= self.buff4Cnt:
                self.buff4Ptr = 0

        return ptr
