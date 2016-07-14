#include <stdio.h>

int main(void)
{
    int i, j, k;

    // 1

    i = 1;
    j = 2;
    k = ++i + j++;

    printf("%d %d %d\n", i, j, k);

    // 2

    i = 1;
    j = 2;
    i = i + 1;
    k = i + j;
    j = j + 1; 

    printf("%d %d %d\n", i, j, k);

    // 3

    i = 1;
    j = 2;
    k = i++ + j++; 

    printf("%d %d %d\n", i, j, k);

    // 4

    i = 1;
    j = 2;
    k = i + j;
    i = i + 1;
    j = j + 1; 

    printf("%d %d %d\n", i, j, k);

    return 0;
}