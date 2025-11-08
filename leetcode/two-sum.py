class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = 0

        #Keep track of the Indexes
        indexOf = {}

        for i, num in enumerate(nums):
            targetNeeded = target - num  # remaining number
            if targetNeeded in indexOf:  # if complement found
                return [indexOf[targetNeeded], i]  # return both indices
            indexOf[num] = i  # store current number and index