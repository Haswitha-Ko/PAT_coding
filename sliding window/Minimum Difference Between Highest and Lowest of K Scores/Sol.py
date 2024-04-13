class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f=[]
        nums.sort()
        d=float('inf')
        for i in range(len(nums)-k+1):
            diff=abs(nums[i]-nums[i+k-1])
            d=min(diff,d)
        return d
        
