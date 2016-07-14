#include <stdio.h>

int main(void)
{
    int a = 5, b = 7, max;

    if (a > b)
        max = a;
    else
        max = b;

    printf("Max from %d and %d is %d\n", a, b, max);

    if (a % 2 == 0)
        printf("%d is even\n", a);

    return 0;
}