int mostWordsFound(char** sentences, int sentencesSize) {
    int max = 0;
    int i = 0;
    for (i=0; i<sentencesSize; i++) {
        int word = 1;
        for (int j = 0; sentences[i][j] != '\0'; j++) {
            if (sentences[i][j] == ' ') {
                word++;;
            }
        } if (word > max) {
            max = word;
        }
    } return max;
}