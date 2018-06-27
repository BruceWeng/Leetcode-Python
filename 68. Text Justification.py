"""
Given an array of words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you
can in each line. Pad extra spaces ' ' when necessary so that each line has exactly
maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number
of spaces on a line do not divide evenly between words, the empty slots on the left
will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted
between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains
             only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
"""
Algorithm: Round Robin
1. "Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right"

It is another word for Round Robin add space after each word(except last word)

2. Declare result[] maintain the result
           one_line_words[] maintain words in each line
           number_of_letters = 0 maintain the number of letters in one_line_words[]
3. The number of spaces allow to add in one_line are (maxWidth - number_of_letters)
4. Round Robin add space:
    for i in range(maxWidth - number_of_letters):
        one_line_words[i%(len(one_line_words)-1 or 1)] += " "
    Note: or 1 handles edge case that the array is empty
5. The timing that start to round robin:
    for w in words:
    number_of_letters + len(one_line_words) + len(w) > maxWidth
    5.a result.append(""join(one_line_words))
    5.b Reset number_of_letters and one_line_words
6. Join the rest of the words in one_line_words with space and fills spaces until
   len(one_line_words) == maxWidth
   6.a add the last line of words to result
7. Return result

T: O(n + maxWidth)
S: O(n + maxWidth)
"""
def fullJustify(words, maxWidth):
    result = []
    one_line_words = []
    number_of_letters = 0

    for w in words:
        if number_of_letters + len(one_line_words) + len(w) > maxWidth:
            # Start round robin
            for i in range(maxWidth - number_of_letters):
                one_line_words[i%(len(one_line_words)-1 or 1)] += " "

            result.append("".join(one_line_words))

            # one_line_words and number_of_letters
            one_line_words = []
            number_of_letters = 0

        # Still have space to add new word in one_line_words
        one_line_words.append(w)
        number_of_letters += len(w)

    # Join the rest of the words in one_line_words with space and fills spaces until
    # len(one_line_words) == maxWidth
    list_of_lastline = list(" ".join(one_line_words))
    while len(list_of_lastline) < maxWidth:
        list_of_lastline.append(" ")

    result.append("".join(list_of_lastline))
    return result

words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
print(fullJustify(words1, maxWidth1))
