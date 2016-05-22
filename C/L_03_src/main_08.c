#include <stdio.h>

int main(void)
{
    int d, i1, i2, i3, i4, i5, j1, j2, j3, j4, j5, s1, s2, total;

    printf("Enter the first (single) digit: ");
    scanf("%1d", &d);
    printf("Enter first group of five digits: ");
    scanf("%1d%1d%1d%1d%1d", &i1, &i2, &i3, &i4, &i5);
    printf("Enter second group of five digits: ");
    scanf("%1d%1d%1d%1d%1d", &j1, &j2, &j3, &j4, &j5);

    s1 = d + i2 + i4 + j1 + j3 + j5;
    s2 = i1 + i3 + i5 + j2 + j4;

    total = 3 * s1 + s2;

    printf("Check digit: %d\n", 10 - total % 10);

    return 0;
}