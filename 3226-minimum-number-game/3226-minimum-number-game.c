#include <stdlib.h>

// Helper: simple selection sort (ascending) — O(n^2) but numsSize <= 100 so it's fine.
void selection_sort(int *a, int n) {
    for (int i = 0; i < n - 1; ++i) {
        int min_idx = i;
        for (int j = i + 1; j < n; ++j) {
            if (a[j] < a[min_idx]) min_idx = j;
        }
        // swap a[i] and a[min_idx]
        int tmp = a[i];
        a[i] = a[min_idx];
        a[min_idx] = tmp;
    }
}

/**
 * Note: The returned array must be malloced; caller should free it.
 */
int* numberGame(int* nums, int numsSize, int* returnSize) {
    // Set the size that we'll return
    *returnSize = numsSize;

    // Allocate output array
    int* arr = (int*) malloc(numsSize * sizeof(int));
    if (arr == NULL) return NULL; // malloc failed (rare on small sizes)

    // Sort nums in-place
    selection_sort(nums, numsSize);

    // Build result: for each pair (nums[i], nums[i+1]) append nums[i+1], nums[i]
    int idx = 0;
    for (int i = 0; i < numsSize; i += 2) {
        arr[idx++] = nums[i + 1]; // Bob's append (the larger of the pair)
        arr[idx++] = nums[i];     // Alice's append (the smaller)
    }

    return arr;
}
