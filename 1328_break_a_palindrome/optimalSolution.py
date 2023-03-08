class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ""
        
        for i in range(int(len(palindrome)/2)):
            if palindrome[i] != 'a':
                palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                return palindrome

        palindrome = palindrome[:len(palindrome)-1] + 'b'
        return palindrome
