class Solution {
    public int findClosestNumber(int[] nums) {
        
        int closestNum = nums[0];

        for(int x: nums){
            int ax = Math.abs(x);
            int ac = Math.abs(closestNum);

           if(ax < ac || (ax == ac && x > closestNum)) { 
            closestNum = x;
        }
        }
        //hi
        return closestNum;
    }
}