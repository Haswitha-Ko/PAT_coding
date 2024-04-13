class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1=set()
        ans=0
        s=0
        i=0
        for j in range(len(nums)):
            while nums[j] in s1:
                s1.remove(nums[i])
                s-=nums[i]
                i+=1
            s1.add(nums[j])
            s+=nums[j]
            ans=max(ans,s)
        return ans
