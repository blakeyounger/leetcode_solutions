class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        
        #create a hashmap with the structure { value: frequency}

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                thirdVal = -nums[i] - nums[j]
                if thirdVal in hashmap and i not in hashmap[thirdVal] and j not in hashmap[thirdVal]:
                    output.append([nums[i], nums[j], thirdVal])
        return output
