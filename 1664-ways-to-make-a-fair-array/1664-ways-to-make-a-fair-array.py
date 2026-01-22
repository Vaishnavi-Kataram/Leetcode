class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_even = 0
        total_odd = 0

        # Step 1: total sums
        for i,num in enumerate(nums):
            if i%2==0:
                total_even += num
            else:
                total_odd += num

        count = 0
        left_even = 0
        left_odd = 0

        # Step 2: try removing each index
        for i, num in enumerate(nums):
            if i%2==0:
                total_even -= num
            else:
                total_odd -= num

            # After removal, right side flips parity
            new_even = left_even + total_odd
            new_odd = left_odd + total_even

            if new_even == new_odd:
                count +=1

            # move current element to left side
            if i%2==0:
                left_even += num
            else:
                left_odd += num

        return count
        