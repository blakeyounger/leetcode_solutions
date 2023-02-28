class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #create a hashmap of each value and the number of occurances
        hashmap = {}

        for i, n in enumerate(arr):
            #if n does not exist in the hashmap, add it and set number of occurances to 1
            if n not in hashmap:
                hashmap[n] = 1
            #else increment it by 1
            else:
                hashmap[n] += 1
        
        list_of_occurances = []
        #now we have the number of occurances for each number. lets check if they are unique
        for key, value in hashmap.items():
            if value in list_of_occurances:
                return False
            list_of_occurances.append(value)
        return True
