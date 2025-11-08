class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} #Storing the values on a hash

        lenOfString = len(s) #getting the length of the string
        summVar = 0 #This is used to sum the values
        i = 0 #Loop

        while i < lenOfString: #Loop 
            if i < lenOfString - 1 and d[s[i]] < d[s[i+1]]: #Checks if the index is less than the last index on the String
                summVar += d[s[i+1]] - d[s[i]] #Sums the 2 variables after a substraction
                i += 2 #Advanced 2 positions
            else:
                summVar += d[s[i]]
                i += 1
        return summVar