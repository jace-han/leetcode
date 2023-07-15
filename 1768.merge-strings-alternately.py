#
# @lc app=leetcode id=1768 lang=python
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ''
        longer = max(word1, word2, key = len)
        count = min(len(word1), len(word2))
        i = 0 

        while count > i:
            merged += word1[i]
            merged += word2[i]
            i += 1

        merged += longer[i:]
        return merged
# @lc code=end

