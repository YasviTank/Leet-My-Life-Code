#include <string.h>  // for strlen
#include <stdbool.h> // for bool, true, false

char* firstPalindrome(char** words, int wordsSize) {
    for (int i = 0; i < wordsSize; i++) {
        int len = strlen(words[i]);
        bool isPalindrome = true;

        // Check palindrome by comparing characters from both ends
        for (int j = 0; j < len / 2; j++) {
            if (words[i][j] != words[i][len - 1 - j]) {
                isPalindrome = false;
                break;  // No need to check further for this word
            }
        }

        if (isPalindrome) {
            return words[i]; // Return the first palindrome found
        }
    }

    // If no palindrome found, return empty string
    return "";
}
