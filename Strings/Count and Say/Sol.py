class Solution:
    def countAndSay(self, n: int) -> str:
        j=1
        s="1"
        while j<n:
            c=1
            strs=s
            s=""
            for i in range(1,len(strs)):
                if strs[i]==strs[i-1]:
                    c+=1
                else:
                    s+=str(c)+strs[i-1]
                    c=1
            s+=str(c)+strs[-1]
            j+=1
        return s
