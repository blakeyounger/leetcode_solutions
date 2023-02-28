class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #sort the array
        nums.sort()
        #loop through array, if it contains duplicate then return True
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
