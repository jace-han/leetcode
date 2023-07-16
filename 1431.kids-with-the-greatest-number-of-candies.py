#
# @lc app=leetcode id=1431 lang=python
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = max(candies)
        res = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= n:
                res.append(True)
            else:
                res.append(False)
    

        return res
# @lc code=end

