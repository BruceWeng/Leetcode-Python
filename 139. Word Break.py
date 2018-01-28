"""
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated sequence
of one or more dictionary words. You may assume the dictionary does not contain
duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set
of strings). Please reload the code definition to get the latest changes.
"""
"""
Algorithm:
1. Initiate result = [False] * len(s) + 1
2. find s[3] == word in wordDict and result[3 - 4]: result[3] = True
3. find s[7] == word in wordDict and result[7 - 4]: result[7] = True
3. return result[-1]
"""
"""
@param {string} s
@param {[]} wordDict
@return {bool}
"""
def wordBreak(s, wordDict):
    if s == None or len(s) == None or wordDict == None or len(wordDict) == 0:
        return False

    result = [False] * (len(s) + 1)
    result[0] = True # starting with one extra dumb space
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if s[i - len(word):i] == word  and result[i - len(word)]:
                result[i] = True
                break

    return result[-1]

if __name__=="__main__":
    print(wordBreak("leetcode", ["leet", "code"]))
