class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''f=[]
        for i in range(k,len(nums)+1):
            sub=nums[i-k:i]
            f.append(sum(sub)/k)
        return max(f)'''
        n=len(nums)
        s=sum(nums[:k])
        ans=s
        for i in range(k,n):
            s+=nums[i]
            s-=nums[i-k]
            ans=max(ans,s)
        return ans/k
