class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #create vowel list
        vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        #create head index
        headIndex = 0

        #create tail index
        tailIndex = len(s) - 1
        
        letterList = []
        for letter in s:
            letterList.append(letter)

        while headIndex <= tailIndex:
            headVowel = ''
            tailVowel = ''
            if letterList[headIndex] in vowelList:
                headVowel = letterList[headIndex]
            else:
                headIndex += 1
            if letterList[tailIndex] in vowelList:
                tailVowel = letterList[tailIndex]
            else:
                tailIndex -= 1
            if headVowel != '' and tailVowel != '':
                #swap the vowels
                letterList[headIndex] = tailVowel
                letterList[tailIndex] = headVowel
                headIndex += 1
                tailIndex -= 1
        
        vowelSwappedString = ""
        for letter in letterList:
            vowelSwappedString += letter
        return vowelSwappedString
