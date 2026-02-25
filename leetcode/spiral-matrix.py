class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        List<Integer> result = new ArrayList<>();

        //Our four pointers
        int left = 0;
        int right = matrix[0].length - 1;
        int top = 0;
        int bottom = matrix.length - 1;

        //While loop for the whole traversal
        while(left <= right && top <= bottom){
        
        //First travel to i --> right
        for(int i = left; i <= right; i++){
            result.add(matrix[top][i]);
        }
        top++;

        //Second Travel down from i
        for(int i = top; i <= bottom; i++){
            result.add(matrix[i][right]);
        }
        right--;

        //Third Travel would be implemented if top <= bottom
        if(top <= bottom){
            for(int i = right; i >= left; i--){
                result.add(matrix[bottom][i]);
            }
        }
        bottom--;

        //Check the condition of left being less or equal to the right, remember they should not end up together
        if(left <= right){
        //Last Travel would be implemented going upwards
        for(int i = bottom; i >= top; i--){
            result.add(matrix[i][left]);
        }
        left++;
        }
        }

        return result;


    }
}