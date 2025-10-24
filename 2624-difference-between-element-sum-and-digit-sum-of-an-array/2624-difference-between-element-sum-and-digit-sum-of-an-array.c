int differenceOfSum(int* nums, int numsSize) {
    int esum = 0;
    int dsum = 0;
    int i;
    for (i=0; i<numsSize; i++) {
        esum += nums[i];
        int digit;
        while (nums[i]) {
            digit = nums[i] % 10;
            dsum += digit;
            nums[i] = nums[i] / 10;
        }
    }return (esum - dsum);
}