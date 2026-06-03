class Solution {
    public int maxProfit(int[] prices) {
        int left=0;
        int n=prices.length;
        int maxProfit=0;

        for(int right=1;right<n;right++){
            //cheaper day to buy
            if(prices[right]<prices[left]){
                left=right;
            }
            else{
                int profit=prices[right]-prices[left];
                maxProfit=Math.max(maxProfit, profit);
            }
            
        }
        return maxProfit;
        
    }
}
