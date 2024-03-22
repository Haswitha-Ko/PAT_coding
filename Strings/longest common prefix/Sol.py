class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''s=""
        l=set()
        for i in strs:
            l.add(i[0])
            if len(l)>0:
                return("")
            else:
                while len(strs[0])!=0:'''
        if len(strs)<2:
            return strs[0]
        strs.sort()
        prefix=""
        i=0
        while i<len(strs[0]) and i<len(strs[-1]):
            if strs[0][i]==strs[-1][i]:
                prefix+=strs[0][i]
                i+=1
            else:
                break
        return prefix
