class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) == 0:
            return ""

        toArray = s.split(" ")
        length = len(toArray)
        start = 0
        end = length - 1
        while start < end:
            temp = toArray[start]
            toArray[start] = toArray[end]
            toArray[end] = temp

            start += 1
            end -= 1

        result = " ".join(toArray)
        return result

test1 = "ya the sky is blue"
solution = Solution()
print solution.reverseWords(test1) #"blue is sky the"
