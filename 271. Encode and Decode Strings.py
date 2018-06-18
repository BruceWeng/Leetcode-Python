"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters.
Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and
decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should
implement your own encode/decode algorithm.
"""
"""
Algorithm:
Encode: convert the array of strings to a single line string by the rule of str.length + '/' + str + str.length + '/' + str...
Decode: declare an empty array result to store the strings
1. find the idx = s[i:].indexOf('/')
2. determine size = int(s[i:i+idx])
3. result.append(s[i+idx+1:i+idx+size+1])
4. i += idx+size+1
5. return result

Ex:
input1 = ['hello', 'bruce']
encode(input1) = '5/hello5/bruce

i = 0:
idx = 1, size = s[0:0+1] = 5, firstString = s[0+1+1:0+1+5+1] = s[2:7] = hello, i = 0 + 1 + 5 + 1 = 7

i = 7:
idx = s[7:].indexOf('/') = 1, size = s[7:7 + 1] = 5, secondString = s[7+1+1:7+1+5+1] = s[9:14] = bruce, i = 7 + 1 + 5 + 1 = 14

Even input contains '/', for "ab/cd", the encoded one should be "5/ab/cd". The decode
function will read the length first, then skip the slash between '5' and 'a', starting
from the next character and get the substring of that length which is "ab/cd".
"""
class Codec:
    """
    @param {str[]} strs
    @return {str} encoded string
    """
    def encode(self, strs):
        if strs == None or len(strs) == 0:
            return ""

        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append('/')
            result.append(s)
        return "".join(result)

    """
    @param {str} s
    @return {str[]}
    """
    def decode(self, s):
        if s == None or len(s) == 0:
            return []

        result = []
        i = 0
        while i < len(s):
            idx = s[i:].find('/')
            size = int(s[i:i+idx])
            result.append(s[i+idx+1:i+idx+size+1])
            i += idx + size + 1
        return result

input1 = ["hello", "bruce"]
codec = Codec()
print(codec.encode(input1))
