int arraySign(int* nums, int numsSize) {
    int i;
    int prod = 1;
    int m;
    for(i=0; i<numsSize; i++) {
        if (nums[i] > 0) {
            m = 1;
        } else if (nums[i] < 0) {
            m = -1;
        } else {
            m = 0;
        } prod *= m;
    } return prod;
}