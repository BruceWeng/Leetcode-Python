"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
"""
"""
Algorithm:
Compare if word1 == word2 first and save as same(bool).
If same:
    when find first word1 match, assign index to idx1 and then swap(idx1, idx2)
"""
"""
@param {str[]} words
@param {str} word1
@param {str2} word2
"""
import sys
def shortestWordDistance(words, word1, word2):
    same = word1 == word2
    idx1 = -1
    idx2 = -1
    minDiff = sys.maxsize

    for i in range(len(words)):
        if words[i] == word1:
            idx1 = i
            if same:
                temp = idx1
                idx1 = idx2
                idx2 = temp
        elif words[i] == word2:
            idx2 = i

        if idx1 != -1 and idx2 != -1:
            minDiff = min(minDiff, abs(idx1 - idx2))

    return minDiff
