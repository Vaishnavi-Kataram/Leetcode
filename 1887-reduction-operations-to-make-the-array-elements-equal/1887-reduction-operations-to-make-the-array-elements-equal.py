class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        ans=0

        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                ans+=i
        return ans
