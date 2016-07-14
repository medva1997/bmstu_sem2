/*
Слайд 13
*/

#include <stdio.h>

int main(void)
{
    int digits, n = 157;

    do
    {
        digits++;
        n /= 10;
    }
    while (n != 0);

    printf("The number has %d digit(s).\n", digits);

    return 0;
}