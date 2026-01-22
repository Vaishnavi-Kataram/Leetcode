class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        prefix_sum =0
        seen = {0: -1}
        min_len = len(nums)

        for i,num in enumerate(nums):
            prefix_sum += num
            cur_rem = prefix_sum % p
            needed = (cur_rem - remainder) % p

            if needed in seen:
                min_len = min(min_len, i-seen[needed])

            seen[cur_rem] = i

        return min_len if min_len < len(nums) else -1
        