class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s=str(num)
        c=0
        for i in range(k,len(s)+1):
            d=int(s[i-k:i])
            if d!=0 and num%d==0:
                c+=1
        return c
