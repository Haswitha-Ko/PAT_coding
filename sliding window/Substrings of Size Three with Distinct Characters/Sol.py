class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(3,len(s)+1):
            substr=s[i-3:i]
            c=set(substr)
            if len(c)==3:
                count+=1
        return count
