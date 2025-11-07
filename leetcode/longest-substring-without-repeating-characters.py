class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #HashSet to store unique values
        hashSett = {}

        #Creation of the window
        leftWindow = 0

        #store the longestSubString
        longestSub = 0
        
        #Loop for getting values
        for i in range(len(s)):
            #s[i] in hs means if the character is inside the hashSett / hs[s[i]] >= left
            if s[i] in hashSett and hashSett[s[i]] >= leftWindow:
            #Update the leftWindow
                leftWindow = hashSett[s[i]] + 1
            #Update the HashSet with the new Value
            hashSett[s[i]] = i
            #Find the longest subs between the windows
            longestSub = max(longestSub, i - leftWindow + 1)

        return longestSub  # <-- Indented to match the for loop level