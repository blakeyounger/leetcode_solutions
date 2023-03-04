class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        numPairs = 0
        for leftIndex in range(len(time)-1):
            for rightIndex in range(leftIndex+1, len(time)):
                if (time[leftIndex] + time[rightIndex]) % 60 == 0:
                    numPairs += 1

        return numPairs
