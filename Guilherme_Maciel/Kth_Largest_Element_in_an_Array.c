#include <stdio.h>
void troca(int* a, int* b);
int particao(int* nums, int esq, int dir);

int findKthLargest(int* nums, int numsSize, int k) {
    int esq = 0, dir = numsSize - 1;
    int maiorNum = numsSize - k;
    while (esq <= dir) {
        int indicePivo = particao(nums, esq, dir);
        if(indicePivo == maiorNum)
          return nums[indicePivo];
        else if(indicePivo <maiorNum)
          esq = indicePivo + 1;
        else
          dir = indicePivo - 1; 
    }
    return -1;
}
void troca(int* a, int* b) {
    int temp = *a; 
    *a = *b; 
    *b = temp;
}

int particao(int* nums, int esq, int dir) {
    int pivo = nums[dir]; 
    int i = esq;
    for (int j = esq; j < dir; j++) {
        if(nums[j] <= pivo) {
            troca(&nums[i], &nums[j]);
            i++;
        }
    }
    troca(&nums[i], &nums[dir]);
    return i;
}
