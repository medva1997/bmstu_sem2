/*
Слайд 26
*/

#include <stdio.h>

int main(void)
{
    int d, n = 21;

    // Определение "простоты" числа

    for (d = 2; n % d != 0 && d < n; d++)
        ;

    if (d < n)
        printf("%d is divisible by %d\n", n, d);
    else
        printf("%d is prime\n", n);

    return 0;
}