"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
"""
Corner case:
Input: "" -> []
Input: "not valid string" -> []
"""
"""
Algorithm:
0. Initial result []
1. Define inValid(s):
    a. len(s) == 0
    b. int(s) > 255
    c. len(s) > 1 and s[0] == "0"
    d. len(s) > 3
2. Define traverse(current, s, k)
    current: result cadidate, from s[0:i] that pass inValid cases + "."
    s: s[i:]
    k: the kth ip number
3. dfs:
    a. base case:
        if len(s) == 0 and k == 4:
            result.append(current)
            return
    b. recursion case:
        for i in range(3):
            if len(s) >= i and isValid(s[:i]):
                if k == 3:
                    traverse(current + s[:i], s[i:], k + 1)
                else:
                    traverse(current + s[:i] + ".", s[i:], k + 1)
"""
"""
@param {string} s
@return {string[]}
"""
def restoreIPAddresses(s):
    if len(s) < 4 or len(s) > 12:
        return []

    result = []

    def isValid(s):
        if len(s) == 0 or int(s) > 255 or (len(s) > 1 and s[0] == "0") or len(s) > 3:
            return False
        return True

    def traverse(current, s, k):
        if len(s) == 0 and k == 4:
            result.append(current)
            return
        for i in range(1, 4):
            if len(s) >= i and isValid(s[:i]):
                if k == 3:
                    traverse(current + s[:i], s[i:], k + 1)
                else:
                    traverse(current + s[:i] + ".", s[i:], k + 1)

    traverse("", s, 0)
    return result

if __name__=="__main__":
    print(restoreIPAddresses("25525511135"))
