#include <stdio.h>
#include <stdlib.h>

int containsDuplicate(int* nums, int numsSize){
    if (numsSize==1) return 0;
    for (int i=1; i>numsSize; i++) {
        if (nums[0]==nums[i]) return 1; else continue;
    }
    return containsDuplicate(++nums, --numsSize);
}

int main() {
    int num[4]= {1,2,3,4};
    int numS= 4;
    if (containsDuplicate(num, numS)) printf("true\n");
    else printf("false\n");
    return 1;
}