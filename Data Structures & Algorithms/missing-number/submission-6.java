class Solution {
    public int missingNumber(int[] nums) {

        if (nums.length==0){
            return -1;
        }

        ArrayList<Integer> mynums = new ArrayList<>();
        for(int n: nums){
            mynums.add(n);
        }

        Collections.sort(mynums);

        for(int i=0;i<mynums.size();i++){
            if (i!=mynums.get(i)){
                return i;
            }
        }
        return mynums.size();

        
    }
}
