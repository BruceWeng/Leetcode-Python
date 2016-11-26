class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        heights = [int(matrix[0][j]) for j in range(len(matrix[0]))]
        maxValue = self.largestRectangleArea(heights)

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1

            maxValue = max(maxValue, self.largestRectangleArea(heights))
        return maxValue


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

        for i in range(1, len(heights)):

            if heights[i] >= hStack[len(hStack) - 1]:
                hStack.append(heights[i])
                sIdxStack.append(i)

            else:
                while hStack and heights[i] < hStack[len(hStack) - 1]:
                    sIdxTop = sIdxStack.pop()
                    hTop = hStack.pop()
                    maxValue = max(maxValue, (i - sIdxTop) * hTop)

                hStack.append(heights[i])
                sIdxStack.append(sIdxTop)

        while sIdxStack:
            sIdxTop = sIdxStack.pop()
            hTop = hStack.pop()
            maxValue = max(maxValue, (len(heights) - sIdxTop) * hTop)

        return maxValue

sol = Solution()
test1 = ["10100","10111","11111","10010"]
test2 = ["01", "10"]
print sol.maximalRectangle(test2)
