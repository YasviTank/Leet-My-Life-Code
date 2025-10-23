#include <stdbool.h>  // for bool, true, false
#include <string.h>   // for strlen()



bool checkIfPangram(char* sentence) {
    int seen[26] = {0};
    int count = 0;

    for (int i = 0; i < strlen(sentence); i++) {
        char c = sentence[i];

        if (c >= 'a' && c <= 'z') {
            int index = c - 'a';    // find position (0–25)

            // if we haven't seen this letter before
            if (seen[index] == 0) {
                seen[index] = 1;     // mark it as seen
                count++;             // increase unique letter count

                // if all 26 found, we can stop early
                if (count == 26)
                    return true;
            }
        }
    }

    // if after scanning all, count < 26 → not pangram
    return (count == 26);
}