"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
"""
@params {string[]} words
@return {string[]}
"""
def findWords(words):
    if words == None or len(words) == 0:
        return []
    result = []
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    table = {} # key: character, value: row index
    # initiate index
    for i in range(len(rows)):
        for char in rows[i]:
            table[char] = i
    # find valid word
    for word in words:
        if word == "":
            continue
        index = table[word[0].lower()]
        for i in range(1, len(word)):
            if index != table[word[i].lower()]:
                index = -1
                break
        if index != -1:
            result.append(word)
    return result
