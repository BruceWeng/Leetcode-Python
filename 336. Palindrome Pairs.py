"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the
given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
"""
Algorithm: HashMap
1. Check each word for prefixes. If find a prefix that is a valid palindrome,
the suffix reversed can be paired with word, prepend the reversed suffix to the current word

2. Check each word for suffixes. If find a suffix that is a valid palindrome,
the prefix reversed can be paired with word, append the reversed prefix to the current word

3. By considering the palindrome of the empty string as prefix for the other word,
we avoid empty string case when considering suffixes to avoid counting duplicates

4. Use a hashmap words(word, index) to store word, index pairs

T: O(n * k^2), n: words list size, k: longest word size
S:
    hashMap: O(n)
    isPalindrome: O(k^2)
    Total: O(n * k^2)
"""
"""
@param {str[]} words
@return {[[int]]}
"""
def palindromePairs(words):
    if len(words) == 0:
        return []

    wordMap = {word: i for i, word in enumerate(words)}
    result = []

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            # Check isPalindrome, Check each word for prefixes
            if prefix == prefix[::-1] and suffix[::-1] != word and suffix[::-1] in wordMap:
                result.append([ wordMap[suffix[::-1]], i ])

            # Check isPalindrome, Check each word for suffixes, skip empty string in suffix
            if j != len(word) and suffix == suffix[::-1] and prefix[::-1] != word and prefix[::-1] in wordMap:
                result.append([ i, wordMap[prefix[::-1]] ])

    return result
