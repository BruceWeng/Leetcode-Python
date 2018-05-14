"""
You are playing the following Bulls and Cows game with your friend: You write down
a number and ask your friend to guess what the number is. Each time your friend makes
a guess, you provide a hint that indicates how many digits in said guess match your
secret number exactly in both digit and position (called "bulls") and how many digits
match the secret number but locate in the wrong position (called "cows"). Your friend
will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess,
use A to indicate the bulls and B to indicate the cows. In the above example, your
function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits,
for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and
your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits,
and their lengths are always equal.
"""
"""
Algorithm:
Solution 1: Use one int[] and iterate twice
1. Iterate over secret and count bulls:
    if secret[i] == guess[i]: bulls += 1
    else: numbers[secret[i]]
2. Iterate over secret and count cows:
    if secret[i] != guess[i] and numbers[guess[i]]:
        cows += 1
        m[guess[i]] -= 1
3. return bulls + "A" + cows + "B"

T: (2n), S: (n)

Solution 2: Use one int[] and iterate once
1. Iterate over numbers in secret and in guess and count all bulls right away.
2. Maintain an array that stores count of the number appearances in secret(increament) and in guess(decreasement).
3. If numbers[s] < 0: Number shows in guess before, match cow now, cows += 1
4. If numbers[g] > 0: Number shows in secret before, match cow now, cows += 1
5. return bulls + "A" + cows + "B"

T: (n), S(n)
"""
"""
Solution 2
@param {string} secret
@param {string} guess
@return {string}
"""
def getHint(secret, guess):
    bulls = 0
    cows = 0
    numbers = [0] * 10
    for i, val in enumerate(secret):
        s = int(secret[i])
        g = int(guess[i])
        if s == g:
            bulls += 1
        else:
            # Number shows in guess before, now match cows
            if numbers[s] < 0:
                cows += 1
            # Number shows in secret before, now match cows
            if numbers[g] > 0:
                cows += 1
            numbers[s] += 1
            numbers[g] -= 1
    return str(bulls) + "A" + str(cows) + "B"
