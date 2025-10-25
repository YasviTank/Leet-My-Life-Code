#include<stdlib.h>
int countKeyChanges(char* s) {
    int i;
    int count = 0;
    for(i=0; i < strlen(s) - 1; i++) {
            if (s[i] == s[i+1] || (s[i]-32) == s[i+1] || (s[i] + 32) == s[i+1]){
                continue;
            }else{
                count+=1;
            }
    }return count;
}