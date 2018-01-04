class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        if lens <= numRows :
            return s
        
        i = 0
        list = [""] * numRows
        while i < lens :
            j = 0
            while j < numRows and i < lens :
                list[j] += s[i]
                j += 1
                i += 1
            j = numRows - 2
            while j >= 1 and i < lens :
                list[j] += s[i]
                j -= 1
                i += 1
        sss = ""
        for ss in list :
            sss += ss
        return sss