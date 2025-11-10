import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        //Create a temp List for
        List<String> ans = new ArrayList<>();

        //Length
        int len = nums.length;
        int i = 0;

        while(i < len){
            //Save the point on the  nums[i]
            int StartPoint = nums[i];
            
            //loop to increment i while is a sum of 1
            while(i < len - 1 && nums[i] + 1 == nums[i + 1]){
                i++;
            }

            //Check if start point is not equal to the inital value after the increment
            if(StartPoint != nums[i]){
                ans.add(StartPoint + "->" + nums[i]);
            }
            //added them anyways
            else{
                ans.add(String.valueOf(nums[i]));
            }
            i++;
        }
        return ans;

    }
}