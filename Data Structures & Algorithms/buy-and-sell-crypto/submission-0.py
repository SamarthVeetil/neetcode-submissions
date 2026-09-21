class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 0
        mP = 0

        while s < len(prices):
            if prices[s] > prices[b]:
                profit = prices[s] - prices[b]
                mP = max(mP, profit)
            else:
                b = s
            s += 1
        return mP
                
            
            

                





    




    


    




        

            
        

                    