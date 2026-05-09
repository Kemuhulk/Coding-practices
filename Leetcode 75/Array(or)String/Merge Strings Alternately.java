// Leetcode question no.1768 : Merge Strings Alternately

// Input: word1 = "abc", word2 = "pqr"
// Output: "apbqcr"
    
class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();
        int i = 0, len1 = word1.length(), len2 = word2.length();

        while (i < len1 || i < len2) {
            if (i < len1) merged.append(word1.charAt(i)); // Add from word1
            if (i < len2) merged.append(word2.charAt(i)); // Add from word2
            i++;
        }
        
        return merged.toString();
    }
}
