# T: O(n), S: O(n)
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Thought: allow only 0 or 1 single char -> True
        # Step1: init flag dict
        # Step2: traverse s, if char not in flag: flag[i] = True(single)
        # Step3: if flag[i] == True: flag[i] = False, else: flag[i] = True
        # Step4: for i in flag: if i == True, count += 1
        # Step5: if count > 1: return False, else: return True
        if not s:
            return False

        flag = {}
        count = 0
        for i in s:
            if i not in flag:
                flag[i] = True
                continue
            if flag[i] == True:
                flag[i] = False
            else:
                flag[i] = True

        for j in flag.values():
            if j == True:
                count += 1

        return False if count > 1 else True

    # Solution without count
    def canPermutePalindrome2(self, s):
        if not s:
            return False

        flag = set()
        for i in s:
            if i not in flag:
                flag.add(i)
                continue
            if i in flag:
                flag.remove(i)

        return False if len(flag) > 1 else True

test1 = 'code'
test2 = 'aab'
test3 = 'carerac'
sol =Solution()
print sol.canPermutePalindrome2(test1) # False
print sol.canPermutePalindrome2(test2) # True
print sol.canPermutePalindrome2(test3) # True
