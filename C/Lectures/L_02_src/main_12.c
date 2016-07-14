#include <stdio.h>

int main(void)
{
    int i, j;
    float x, y;

    // 1 -20 .3 -4.0e3
    scanf("%d%d%f%f", &i, &j, &x, &y);

    printf("%d %d %g %e\n", i, j, x, y);

    return 0;
}