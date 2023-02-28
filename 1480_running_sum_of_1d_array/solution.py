class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        tempSum = 0
        for n in nums:
            tempSum += n
            runningSum.append(tempSum)
        return runningSum
