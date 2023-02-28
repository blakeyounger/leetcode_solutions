class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        diff = high - low 

        if high % 2 == 1 or low % 2 == 1:
            return int(math.floor(diff / 2) + 1)
        return diff / 2
