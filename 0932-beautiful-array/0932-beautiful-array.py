class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [1]
        
        while len(res)<n:
            temp = []
            for ele in res:
                if (2*ele - 1)<=n:
                    temp.append(2*ele - 1)
            for ele in res:
                if (2 * ele)<= n:
                    temp.append(2*ele)
            res = temp

        return res


        