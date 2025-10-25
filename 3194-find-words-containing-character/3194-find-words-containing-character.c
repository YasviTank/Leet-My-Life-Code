#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* result = (int*) malloc(sizeof(int) * wordsSize);
    int count = 0;

    for (int i = 0; i < wordsSize; i++) {
        if (strchr(words[i], x) != NULL) {
            result[count++] = i;
        }
    }
    *returnSize = count;
    return result;
}