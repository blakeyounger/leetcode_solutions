class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        #build a hashmap of letter freqencies for word1
        word1Hashmap = {}
        for letter in word1:
            if letter not in word1Hashmap:
                #add the letter to the hashmap
                word1Hashmap[letter] = 1
            else:
                #we've seen this letter before. increment the frequency count   
                word1Hashmap[letter] += 1

        #build a hashmap of letter frequencies for word2 
        word2Hashmap = {}
        for letter in word2:
            if letter not in word2Hashmap:
                #add the letter to the hashmap
                word2Hashmap[letter] = 1
            else:
                #we've seen this letter before. increment the frequency count   
                word2Hashmap[letter] += 1

        #build a list of all letters used in word1 and word2
        letterList = []
        for letter in word1:
            if letter not in letterList:
                letterList.append(letter)
        
        for letter in word2:
            if letter not in letterList:
                letterList.append(letter)

        #for each letter in this list, lookup the frequency in the word1 and word2 hashmap
        for letter in letterList:
            #find the word1 letter frequency
            #if it does not exist in the hashmap, set frequency to 0
            if letter in word1Hashmap:
                word1LetterFrequency = word1Hashmap[letter]
            else:
                word1LetterFrequency = 0
            #find the word2 letter frequency
            #if it does not exist in the hashmap, set frequency to 0
            if letter in word2Hashmap:
                word2LetterFrequency = word2Hashmap[letter]
            else:
                word2LetterFrequency = 0
            
            #calculate the difference between the freqencies
            frequencyDifference = abs(word1LetterFrequency - word2LetterFrequency)

            if frequencyDifference >= 4:
                return False
        
        return True
