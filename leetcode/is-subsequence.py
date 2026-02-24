class Solution {
    public boolean isSubsequence(String s, String t) {

        if(s.length() > t.length()) return false;
        if(s.equals("")) return true;
        
        int A = 0;
        int B = 0;

        while(A < s.length() && B < t.length()){
            
            if(s.charAt(A) == t.charAt(B)){
                A++;
            }
            B++;

            if(A >= s.length()){
                return true;
            }
        } 

        return false;
    }
}