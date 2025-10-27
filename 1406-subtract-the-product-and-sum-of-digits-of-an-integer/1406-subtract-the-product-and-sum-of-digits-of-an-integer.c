int subtractProductAndSum(int n) {
    int temp;
    int sum_digit = 0;
    int prod_digit = 1;

    while(n){
        temp = n%10;
        sum_digit += temp;
        prod_digit *= temp;
        n = n/10;
    } return prod_digit - sum_digit;
}