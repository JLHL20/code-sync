class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '': return True
        if len(s) > len(t): return False
        A = 0
        B = 0

        while A < len(s) and B < len(t):
            if s[A] == t[B]:
                A += 1
            B += 1
        return A == len(s)