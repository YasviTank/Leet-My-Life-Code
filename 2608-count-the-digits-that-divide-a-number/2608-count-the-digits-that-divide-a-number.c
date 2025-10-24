int countDigits(int num) {
    int temp = num;
    int digit = 0;
    int count = 0;
    while (temp) {
        digit = temp % 10;
        if (num%digit == 0) {
            count += 1;
        } temp = temp / 10;
    } return count;
}