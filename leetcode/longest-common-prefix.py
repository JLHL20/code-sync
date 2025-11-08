class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        int min_length = strs[0].length();

        //Track the smallest string inside the array
        for(String s : strs){
            if(s.length() < min_length){
                min_length = s.length();
            }
        }

        int i = 0;
        //Loop inside the String for each characters
        while(i < min_length){
            for(String s : strs){ //Loop inside the Array with s as charAt(i) checking every string in the list strs
                if(s.charAt(i) != strs[0].charAt(i)){  // if the char at s[i] is not equal to the first string we just return
                    return strs[0].substring(0, i); //return the substring
                }
            }
            i++; //Increment
        }
        return strs[0].substring(0, i); //Always return the substring to not get any future errors
    }
}