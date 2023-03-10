class RandomizedSet(object):

    def __init__(self):
        self.listOfVals = []
        self.hashmap={}
        

    def insert(self, val):
        #Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.listOfVals)
        self.listOfVals.append(val)
        return True
        

    def remove(self, val):
        #Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False
        #lookup index
        index = self.hashmap[val]
        self.listOfVals[index] = self.listOfVals[len(self.listOfVals)-1]
        self.hashmap[self.listOfVals[len(self.listOfVals)-1]] = index
        self.listOfVals.pop()
        del self.hashmap[val]
        return True
        

    def getRandom(self):
        #Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
        #Each element must have the same probability of being returned.
        """
        :rtype: int
        """
        randomFloat = random.random()

        scaledRandomFloat = randomFloat * len(self.listOfVals)

        randomIndex = int(math.floor(scaledRandomFloat))
        return self.listOfVals[randomIndex]

