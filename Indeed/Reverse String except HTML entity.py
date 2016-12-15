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
    if strs == None or len(strs) == 0:
        return strs

    tokens = []
    start = 0
    end = 0

    def reverse(strs, start, end):
        if start == 0:
            return ''.join(list(strs)[end::-1])
        return ''.join(list(strs)[end:start-1:-1])


    while end < len(strs):
        if strs[end] != '&':
            end += 1
        else:
            # Step1: Reverse substring before &
            if end != 0:
                token = reverse(strs, start, end - 1)
                tokens.append(token)

            # Step2: Put the HTML entity into the tokens
            temp = ''
            while end < len(strs) and strs[end] != ';':
                temp += strs[end]
                end += 1

            if end < len(strs):
                temp += ';'
                tokens.append(temp)
                # Step3: Update start
                end += 1
                start = end
    # Step1: Reverse the trailing chars
    if start == 0:
        return reverse(strs, start, len(strs) - 1)

    if start < end:
        token = reverse(strs, start, len(strs) - 1)
        tokens.append(token)

    # Step2: Concatenate the Final result
    result = ''
    for i in range(len(tokens) - 1, -1, -1):
        result += tokens[i]

    return result



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
