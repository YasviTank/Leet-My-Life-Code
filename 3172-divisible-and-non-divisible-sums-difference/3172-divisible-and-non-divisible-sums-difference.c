int differenceOfSums(int n, int m) {
    int i;
    int notsum = 0;
    int divsum = 0;
    for (i=1; i<=n; i++) {
        if (i%m == 0) {
            divsum += i;
        } else {
            notsum += i;
        }
    } return notsum - divsum;
}