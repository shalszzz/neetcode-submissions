class Solution {
    public int findDuplicate(int[] nums) {

        int n=nums.length;

        if(n==1 || n==2){
            return nums[0];
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {

                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }

        int left=0;
        int right=1;
        while(right<n){
            if (nums[right]==nums[left]){
                return nums[left];
            }
            left=right;
            right++;
        }
        return 0;



        
    }
}
