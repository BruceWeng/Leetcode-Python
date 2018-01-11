"""
Use a Collection for Scope Variables
A fix would be to create a list and set the first index value to your result.
Then when we access the first element, we will access the scope variable rather
than creating a new local variable.
"""
def recursion(n):
    # Use collection as Scope variable
    result = [1]

    def helper(count):
        # non-local variable are read only by default, ex: n, result
        # base case
        if count > n:
            return
        # recursive case
        result[0] = result[0] * count
        helper(count + 1)
    # invoke helper
    helper(1)
    # return result
    return result[0]

print recursion(3)
