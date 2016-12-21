# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Solution1: Recursion
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        val = 0

        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)

        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)

        return max(root.val + val, self.rob(root.left) + self.rob(root.right))

    # Solution2: DP, HashMap
    def rob2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robSub(root, cache):
            if not root:
                return 0

            val = 0
            if root in cache:
                return cache[root]

            if root.left:
                val += robSub(root.left.left, cache) + robSub(root.left.right, cache)

            if root.right:
                val += robSub(root.right.left, cache) + robSub(root.right.right, cache)

            val = max(root.val + val, robSub(root.left, cache) + robSub(root.right, cache))
            cache[root] = val
            return val

        return robSub(root,{})

    # Solution3: DFS and prune, unrobbed, robbed
    def rob3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robSub(root):
            # rtype: [unrobbed, robbed]
            if not root:
                return [0, 0]
            result = [0, 0] # result[0]: unrobbed, result[1]: robbed

            left = robSub(root.left)
            right = robSub(root.right)
            result[0] = max(left[0], left[1]) + max(right[0], right[1])
            result[1] = root.val + left[0] + right[0]
            return result

        unrobbed, robbed = robSub(root)
        return max(unrobbed, robbed)

    # Solution4: sol3 optimized
    def rob4(self, root):
        def robSub(node):
            #rtype: [unrobbed, robbed or unrobbed]
            if not node:
                return [0,0]

            left = robSub(node.left)
            right = robSub(node.right)
            result = [0, 0]
            result[0] = left[1] + right[1]
            result[1] = max(left[1] + right[1], left[0] + right[0] + node.val)
            return result

        return robSub(root)[1]

    # Solution5: sol4 optimized with tuple
    def rob5(self, root):
        def robSub(node):
            #rtype: (unrobbed, robbed or unrobbed)
            if not node:
                return (0,0)

            left = robSub(node.left)
            right = robSub(node.right)
            return (left[1] + right[1], max(left[1] + right[1], left[0] + right[0] + node.val))

        return robSub(root)[1]

test1 = TreeNode(4)
test1.left = TreeNode(1)
test1.left.left = TreeNode(2)
test1.left.left.left = TreeNode(3)
sol = Solution()
print sol.rob5(test1)
