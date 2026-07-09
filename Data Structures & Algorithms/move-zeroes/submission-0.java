class Solution {
    public void moveZeroes(int[] nums) {
        ArrayList<Integer> rem = new ArrayList<>();
        int count = 0;

        for (int num : nums) {
            if (num != 0) {
                rem.add(num);
            } else {
                count++;
            }
        }

        ArrayList<Integer> result = new ArrayList<>();

        for (int num : rem) {
            result.add(num);
        }

        for (int i = 0; i < count; i++) {
            result.add(0);
        }

        for (int i = 0; i < nums.length; i++) {
            nums[i] = result.get(i);
        }
    }
}