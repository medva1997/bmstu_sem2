#include <stdio.h>

int main(void)
{
    int i = 40;

    printf("|%d|%5d|%-5d|%5.3d|\n", i, i, i, i);

    printf("\n\n\n");

    float f = 839.21f;

    printf("|%10.3f|%10.3e|%-10g|\n", f, f, f);

    return 0;
}