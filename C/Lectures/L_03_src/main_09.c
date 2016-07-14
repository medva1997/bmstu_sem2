#include <stdio.h>

int main(void)
{
    int i, j;

    i = 1;
    j = 2;
    printf("%d\n", (i != 0) && (j / i > 0));

    i = 1;
    j = -2;
    printf("%d\n", (i != 0) && (j / i > 0));

    i = 0;
    j = 2;
    printf("%d\n", (i != 0) && (j / i > 0));

    i = 0;
    j = -2;
    printf("%d\n", (i != 0) && (j / i > 0));

    return 0;
}