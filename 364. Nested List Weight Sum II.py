# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
# Solution: http://www.cnblogs.com/grandyang/p/5615583.html
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if len(nestedList) == 0:
            return 0

        sumValue = 0
        # Init an dict with sum(elements), level = len(dict) - key(index from 0)
        # Not using list because can not assign value to index larger than len(list)
        # ex: [1, 2, [3, 4, [5, 6]], 7, 8] -> { '0': 1+2+7+8, '1': 3+4, '2': 5+6 }
        level = {}
        def dfs(nestedList, depth):
            if str(depth) not in level:
                level[str(depth)] = 0
            if nestedList.isInteger():
                level[str(depth)] += nestedList.getInteger()
                return
            else:
                for ni in nestedList.getList():
                    dfs(ni, depth + 1)

        for ni in nestedList:
            dfs(ni, 0)

        for i in range(len(level)):
            sumValue += (len(level) - i) * level[str(i)]

        return sumValue
