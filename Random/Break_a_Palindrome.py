"""
Given a palindrome, attempt to break the palindrome by replacing 1 single character in the string. 
Return the lexicographically smallest possible string that breaks the palindrome. 
If no such string exists to break the palindrome, return the empty string, ''.
"""

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """

        # palindromes => first-half = second-half[::-1]
        # we store the character count map of 1-half the palindome (ignore the middle if len is odd)
        # even better, don't store the count. just iterate until the first non-'a' char
        # if there is only 1-unique character, and the character is 'a', then no way for smaller-value str
        # if >1 unique character or character is not 'a', then simply replace the first non-'a' with 'a'

        n= len(palindrome)//2
        
        # case 1: len==1 | len//2 == 0
        if n==0: return ''

        # case 2: len//2 == 1
        if n==1: 
            if palindrome[0]=='a': return palindrome[:-1] + 'b'
            else: return 'a' + palindrome[1:]

        # case 3: len//2 >1
        for i in range(n): 
            if palindrome[i]!='a': return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:-1] + 'b'

