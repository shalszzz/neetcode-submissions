class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left=0;
        int maxLen=0;
        int n=s.length();

        HashSet<Character> seen = new HashSet<>();
        
        
        for(int right=0;right<n;right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left++;
                
            }
            seen.add(s.charAt(right));
            int len=right-left+1;
            maxLen=Math.max(maxLen, len);

            
            
            
            
        }
        return maxLen;
        
    }
}
