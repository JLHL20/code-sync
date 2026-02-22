class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        int n = nums.length;
        int[] answer = new int[n];

        int leftSide = 1;
        int rightSide = 1;

        //Left side
        for(int i = 0; i < n; i++){
            answer[i] = leftSide;
            leftSide *= nums[i];
        }

        for(int i = n - 1; i >= 0; i--){
            answer[i] *= rightSide;
            rightSide *= nums[i];
        }

        return answer;

    }
}