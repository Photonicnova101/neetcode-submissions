class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> arr = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            if(arr.containsValue(nums[i])){
                return true;
            }
            arr.put(i,nums[i]);
        }
        return false;
    }
}
