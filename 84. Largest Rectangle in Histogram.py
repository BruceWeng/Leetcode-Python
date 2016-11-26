class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0 or heights == None:
            return 0

        maxValue = 0
        sIdxStack = [0]
        hStack = [heights[0]]
        # sIdxTop = sIdxStack[len(sIdxStack) - 1]
        # hTop = hStack[len(hStack) - 1]

        for i in range(1, len(heights)):

            if heights[i] >= hStack[len(hStack) - 1]:
                hStack.append(heights[i])
                sIdxStack.append(i)
                # print 'sIdxStack: ' + str(sIdxStack)
                # print 'hStack: ' + str(hStack)
                # print 'maxValue: ' + str(maxValue)
                # print 'sIdxTop: ' + str(sIdxStack[len(sIdxStack) - 1])
                # print 'hTop: ' + str(hStack[len(hStack) - 1])
            else:
                while hStack and heights[i] < hStack[len(hStack) - 1]:
                    sIdxTop = sIdxStack.pop()
                    hTop = hStack.pop()
                    maxValue = max(maxValue, (i - sIdxTop) * hTop)

                hStack.append(heights[i])
                sIdxStack.append(sIdxTop)
                # print 'sIdxStack: ' + str(sIdxStack)
                # print 'hStack: ' + str(hStack)
                # print 'maxValue: ' + str(maxValue)
                # print 'sIdxTop: ' + str(sIdxTop)
                # print 'hTop: ' + str(hTop)

        while sIdxStack:
            sIdxTop = sIdxStack.pop()
            hTop = hStack.pop()
            maxValue = max(maxValue, (len(heights) - sIdxTop) * hTop)
            # print 'sIdxStack: ' + str(sIdxStack)
            # print 'hStack: ' + str(hStack)
            # print 'maxValue: ' + str(maxValue)


        return maxValue

test1 = [1, 3, 2, 1, 2]
test2 = [4, 2]
test3 = [2, 1, 5, 6, 2, 3]
test4 = [4, 2, 0, 3, 2, 5]
sol = Solution()
print sol.largestRectangleArea(test4)
