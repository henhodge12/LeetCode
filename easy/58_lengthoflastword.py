# 4/1/24
# we need to find the length of the last word in string s
# the built-in split() function of python is helpful here
# split separates a string into an array of words
# we can specify a delimeter if needed, otherwise it uses whitespace
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()
        return len(s[len(s)-1])
        """
        :type s: str
        :rtype: int
        """
