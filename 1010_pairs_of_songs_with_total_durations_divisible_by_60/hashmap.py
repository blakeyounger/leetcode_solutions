class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """

        #do modulo 60 on each time
        for i in range(len(time)):
            time[i] = time[i] % 60
        
        #loop through time again
            #add to hashmap if it does not exist in in it. if it does increment frequency by one
            #if 60 - t is in hashmap, reduce each frequency by 1, increment counter
        
        songCounter = 0
        timeHashmap = {}

        for t in time:
            if t not in timeHashmap:
                timeHashmap[t] = 1
            else:
                timeHashmap[t] += 1
            

        for t in range(1, 30):
            remainder = 60 - t
            if t in timeHashmap and remainder in timeHashmap:
                if timeHashmap[t] < timeHashmap[remainder]:
                    smaller = timeHashmap[t]
                    larger = timeHashmap[remainder]
                else:
                    smaller = timeHashmap[remainder]
                    larger = timeHashmap[t]
                for combos in range(larger, larger-smaller, -1):
                    songCounter += combos


        #handle the edge case with t = 30
        if 30 in timeHashmap and timeHashmap[30] >= 2:
            songCounter += math.floor(timeHashmap[30] / 2)
        
        #handle the edge case with t = 0
        if 0 in timeHashmap and timeHashmap[0] >= 2:
            while timeHashmap[0] > 0:
                timeHashmap[0] -= 1
                songCounter += timeHashmap[0]
        
        return int(songCounter)
