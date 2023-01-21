def hammingWeight(self, n):
    """
        :type n: int
        :rtype: int
        """
    return sum([1 for n in bin((n)) if n == '1'])
