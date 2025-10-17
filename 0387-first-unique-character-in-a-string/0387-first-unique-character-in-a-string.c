int firstUniqChar(char* s) {
    // Srings are stored as arrays of characters ending with a special symbol called the null character — written as '\0'
    int freq[26] = {0};
    int i;

    for (i = 0; s[i] != '\0'; i++){
        freq[s[i] - 'a']++;
    }

    for (i = 0; s[i] != '\0'; i++){
        if (freq[s[i] - 'a'] == 1){
            return i;
        }
    }
    return -1;
}