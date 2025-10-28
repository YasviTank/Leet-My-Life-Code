int calPoints(char** operations, int operationsSize) {
    int *record = (int *)malloc(sizeof(int) * operationsSize);
    int top = 0;  // stack pointer

    for (int i = 0; i < operationsSize; i++) {
        char *op = operations[i];

        if (strcmp(op, "C") == 0) {
            // Remove last score
            top--;
        } else if (strcmp(op, "D") == 0) {
            // Double last score
            record[top] = 2 * record[top - 1];
            top++;
        } else if (strcmp(op, "+") == 0) {
            // Sum of last two scores
            record[top] = record[top - 1] + record[top - 2];
            top++;
        } else {
            // Convert string to integer and add to record
            record[top] = atoi(op);
            top++;
        }
    }

    int total = 0;
    for (int i = 0; i < top; i++) {
        total += record[i];
    }

    free(record);
    return total;
}
