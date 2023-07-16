#
# @lc app=leetcode id=1071 lang=python
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        res = ""
        
        if str1 + str2 == str2 + str1:
            def hcf(a, b): #no of char in output
                if(b == 0):
                    return a
                else:
                    return hcf(b, a % b)

            return str1[:hcf(len(str1), len(str2))]
        
        else:
            return res

            
        


# @lc code=end

