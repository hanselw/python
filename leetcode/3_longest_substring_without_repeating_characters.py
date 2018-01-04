class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = ""
        end = 0
        for ss in list(s) :
            if ss in b :
                end = end if end > len(b) else len(b)
                b = b.split(ss)[-1]
            b += ss
        return end if end > len(b) else len(b)