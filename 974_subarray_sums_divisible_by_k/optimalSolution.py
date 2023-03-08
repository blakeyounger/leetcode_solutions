class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {
            0 : 1
        }

        res = 0
        sum = 0

        for n in nums:
            sum += n
            diff = sum % k

            #lookup diff in hashmap, if diff does not exist in hashmap return 0
            if diff in hashmap:
                res += hashmap[diff]
                hashmap[diff] += 1
            else:
                hashmap[diff] = 1
        
        return res

