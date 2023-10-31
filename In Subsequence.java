public class Solution {
    public boolean isSubsequence(String s, String t) {
        int sPointer = 0;  // Pointer for string s
        int tPointer = 0;  // Pointer for string t
        
        while (sPointer < s.length() && tPointer < t.length()) {
            // If the current characters match, move the sPointer
            if (s.charAt(sPointer) == t.charAt(tPointer)) {
                sPointer++;
            }
            // Always move the tPointer to check the next character in t
            tPointer++;
        }
        
        // If sPointer reached the end of string s, it means s is a subsequence of t
        return sPointer == s.length();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s1 = "abc";
        String t1 = "ahbgdc";
        System.out.println(solution.isSubsequence(s1, t1));  // Output: true

        String s2 = "axc";
        String t2 = "ahbgdc";
        System.out.println(solution.isSubsequence(s2, t2));  // Output: false
    }
}
