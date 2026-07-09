class Solution {
    public int maxProfit(int[] prices) {
        int minprice= prices[0];
        int maxProfit = 0;
        for(int i=0;i<prices.length;i++){
            minprice = Math.min(minprice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i]-minprice);
        }
        return maxProfit;
        
    }
}
