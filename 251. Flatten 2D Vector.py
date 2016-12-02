class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.result = []
        for row in range(len(vec2d)):
            for col in range(len(vec2d[row])):
                self.result.append(vec2d[row][col])
        self.index = 0
    def next(self):
        """
        :rtype: int
        """
        ans = self.result[self.index]
        self.index += 1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < len(self.result):
            return True
        else: return False

test1 = [[1, 2], [3], [4, 5, 6]]
i, v = Vector2D(test1), []
while i.hasNext(): v.append(i.next())
print v
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
