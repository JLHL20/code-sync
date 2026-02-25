class Solution {
    public int[] sortByBits(int[] arr) {

        Integer[] temp = new Integer[arr.length];

        for(int i = 0; i < arr.length; i++){
            temp[i] = arr[i];
        }

        Arrays.sort(temp, (a, b) -> {
            int A = Integer.bitCount(a);
            int B = Integer.bitCount(b);

            return (A == B) ? a - b : A - B;
        });

        for(int i = 0; i < arr.length; i++){
            arr[i] = temp[i];
        }

        return arr;

    }
}