class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                palindrome = palindrome[:i] + 'a' + palindrome[i+1:]

                #if this new string is not a palindrome, break
                #else
                break
            if i == (len(palindrome)-1):
                #if no letters changed so far, make last letter b
                palindrome = palindrome[:i] + 'b'
                if len(palindrome) <= 1:
                    return ''
        return palindrome
