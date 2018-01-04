class Solution(object):
    def lenPdm(self, s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            return  r - l - 1
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        i = len1 = len2 = mlen = 0
        start = end = 0
        while i < lens :
            len1 = self.lenPdm(s, i, i)
            len2 = self.lenPdm(s, i, i+1)
            slen = len1 if len1 > len2 else len2
            if mlen < slen :
                mlen = slen
                start = i - (mlen-1)/2
                end = i + mlen/2
            i += 1
        return s[start:end+1]
    
    