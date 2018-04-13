"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them,
there may exist one celebrity. The definition of a celebrity is that all the other
n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?"
to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B.
Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the
celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
"""
"""
Algorithm:
1. If candidate knows anyone, find next candidate
2. for i < candidate, check knows(candidate, i) and knows(i, candidate)
3. for i > candidate, check knows(i, candidate)
"""
"""
@param {int} n
@return {int}
"""
def findCelebrity(n):
    if n == None:
        return -1

    candidate = 0
    # if candidate knows anyone, find next candidate (exclude all others who knows at least one)
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    for i in range(n):
        # for i < candidate, if the selected candidate knows anyone or anyone not know the candidate
        if i < candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
        # for i > candidate, already checked in the first loop that if knows(candidate, i),
        # only need to check if knows(i, candidate)
        if i > candidate and not knows(i, candidate):
            return -1

    return candidate
