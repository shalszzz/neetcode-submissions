class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount==0:
            return 0
   
        combos=[]
        smallest = float('inf')

        def check(i,sum):

            nonlocal smallest         

            if i>=len(coins) or sum>amount:
                return
            
            if len(combos)>smallest:
                return 
            
            if sum==amount:
                smallest = min(smallest, len(combos))
                return

            combos.append(coins[i])
            check(i,sum+coins[i])

            combos.pop()
            check(i+1,sum)

        check(0,0)
        if smallest==float('inf'): return -1 
        else: return smallest
        

            
                


