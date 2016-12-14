'''
Reverse string except for HTML entities, i.e, A HTML entities must be treated as an entire word without reverse.

e.g. "1234&euro;" => "&euro;4321"
"1234&euro" => "orue&4321"
"1234&euro;567" => "765&euro;4321"

Understand the problem:
Since a HTML entity must start with "&" and end with ";"
This problem can be solved in a two-step approach.
Step 1: reverse non-html tokens, and store the result into a list. For the HTML entity, do not reverse but just store into the result.
Step 2: construct the final result just concatenate the list in a reverse order.
'''
def reverseHTML(strs):
    result = []
    left = 0
    right = 0
    key = 0
    cache = {}
    flag = False
    for i in range(len(strs)):
        if strs[i] == '&':
            left = i
            flag = True
        elif flag == True and strs[i] == ';':
            right = i
            result.append(strs[left:right + 1])
            temp = []
            flag = False
        elif flag == False:
            result.append(strs[i])
        elif i == len(strs) - 1 and flag == True:
            result += strs[left:i + 1]

    result2 = ''
    for i in range(len(result) - 1, -1, -1):
        if len(result[i]) > 1:
            result2 += ''.join(result[i])
        else:
            result2 += str(result[i])

    return result2

test1 = "1234&euro;"
test2 = "1234&euro"
test3 = "1234&euro;567"
test4 = "&euro;1234567"
test5 = "&euro1234567"
print reverseHTML(test1) # "&euro;4321"
print reverseHTML(test2) # "orue&4321"
print reverseHTML(test3) # "765&euro;4321"
print reverseHTML(test4) # "7654321&euro;"
print reverseHTML(test5) # "7654321orue&"
