int xorOperation(int n, int start) {
    int i;
    int nums[n];
    int xor = 0;
    for (i=0; i<n; i++) {
        nums[i] = start + 2 * i;
        xor ^= nums[i];
    } return xor;
}