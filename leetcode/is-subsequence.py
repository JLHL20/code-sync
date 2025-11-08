class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '': return True 
        if len(s) > len(t): return False
        A = 0 #First Pointer
        B = 0 #Second Pointer

        #Loop through the String
        while A < len(s) and B < len(t):
            #Checks if they are equal
            if s[A] == t[B]:
                A += 1 #Updates First Pointer
            B += 1 #Always Updates Second Pointer
        return A == len(s) #If the First pointer ever gets to the same length means we finish
        #return True, otherwise false