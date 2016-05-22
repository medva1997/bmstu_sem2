#include <stdio.h>

int main(void)
{
    int i = 5;
    float f = 1.5;

    printf("%d %d\n", i);

    printf("%d\n", i, i);

    printf("%d %f\n", f, i);

    return 0;
}