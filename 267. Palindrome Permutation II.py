"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
"""
"""
Algorithm: Backtracking
0. Count if there are more than one odd character
ex: "accc", count a: 1, count c: 3

1. Declare oddsCount = 0, hashmap(char, frequency/2)

2. Iterate s:
    increment hashmap[s[i]]
    if hashmap[s[i]] % 2 == 0:
        oddsCount -= 1
    else:
        oddsCount += 1

3. If oddsCount > 1:
    return result // Not valid

4. Declare mid = "", length = 0

5. Itreate hashMap:
    if val > 0:
        // Odd
        if val % 1 == 1:
            mid = str(val)
            hashMap[key] -= 1
        // even
        hashMap[key] /= 2
        length += hashMap[key]

6. Declare helper(s): //Backtracking
    Termination condition:
    if len(s) == length:
        suffix = s[::-1]
        result.append(s + mid + suffix)
        return

    Recursive condition:
    Iterate hashMap:
    if val > 0:
        hashMap[key] -= 1
        helper(s + str(key))
        hashMap[key] += 1

7. Call helper("")
8. Return result

T: O(n * 2^n)
S: O(n * 2^n)
"""
"""
@param {str} s
@return {str[]}
"""
def generatePalindromes(s):
    result = []
    hashMap = {}
    oddsCount = 0
    # Construct hashMap
    for i in range(len(s)):
        if s[i] not in hashMap:
            hashMap[s[i]] = 1
        else:
            hashMap[s[i]] += 1
        if hashMap[s[i]] % 2 == 1:
            oddsCount += 1
        else:
            oddsCount -= 1

    if oddsCount > 1:
        return result

    mid = ""
    length = 0

    for key, val in hashMap.items():
        if val > 0:
            # Odd
            if val % 2 == 1:
                mid = str(key)
                hashMap[key] -= 1
            # Only store char frequency / 2 since only need half of count
            hashMap[key] /= 2
            length += hashMap[key]

    def helper(prefix):
        if len(prefix) == length:
            result.append(prefix + mid + prefix[::-1])
            return

        for key, val in hashMap.items():
            if val > 0:
                hashMap[key] -= 1
                helper(prefix + str(key))
                hashMap[key] += 1

    helper("")
    return result
