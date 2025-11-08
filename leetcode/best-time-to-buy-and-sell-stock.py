class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallestPrice = float('inf') #Infinity number
        max_profits = 0 #Tracker for the max profit

        
        for price in prices:

            if price < smallestPrice: #Checks if i (price) is smaller than the smallestPrice we have on record 
                smallestPrice = price #Assign
            
            profit = price - smallestPrice #Assign new variable profit to be the actual profit for every i

            if profit > max_profits: #Checks if the profit that we have on track is the bigger than our max
                max_profits = profit
        
        return max_profits