class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ansMap={}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in ansMap:
                return [ansMap[x],i]
            ansMap[nums[i]]=i

        return []

