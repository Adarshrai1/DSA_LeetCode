public class Solution {
    public String decodeAtIndex(String s, int k) {
        long totalLength = 0;

        // Calculate the total length of the decoded string
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                totalLength *= (c - '0');
            } else {
                totalLength++;
            }
        }

        // Traverse the string in reverse to find the kth letter
        for (int i = s.length() - 1; i >= 0; i--) {
            k %= totalLength;
            if (k == 0 && Character.isLetter(s.charAt(i))) {
                return String.valueOf(s.charAt(i));
            }

            if (Character.isDigit(s.charAt(i))) {
                totalLength /= (s.charAt(i) - '0');
            } else {
                totalLength--;
            }
        }

        return ""; // Return an empty string if k is out of bounds.
    }
} //Adarsh