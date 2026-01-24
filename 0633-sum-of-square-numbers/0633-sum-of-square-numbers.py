class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(c ** 0.5) # squareroot of c

        while left <= right:
            total = left * left + right * right

            if total == c:
                return True
            elif total < c:
                left += 1
            elif total > c:
                right -= 1
        
        return False
        