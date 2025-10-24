int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) {
    int i;
    int count = 0;
    for(i=0; i<hoursSize; i++) {
        if (hours[i] >= target) {
            count += 1;
        }
    } return count;
}