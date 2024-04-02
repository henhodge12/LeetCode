# 4/2/2024
# This checks if two strings are isomorphic.
# Isomorphic means each letter in each string can be matched with no error.
# Thinking about it like encryption is the easiest way.
# ord() is python returns the Unicode value of the character
class Solution(object):
    def isIsomorphic(self, s, t):
        alphabets = [0]*256
        alphabett = [0]*256
        for i in range(0, len(s)):
            if alphabets[ord(s[i])] == 0:
                if alphabett[ord(t[i])] == 0:
                    alphabets[ord(s[i])] = ord(t[i])
                    alphabett[ord(t[i])] = ord(s[i])
                else:
                    return False
            elif alphabets[ord(s[i])] != 0 and alphabets[ord(s[i])] != ord(t[i]):
                return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
