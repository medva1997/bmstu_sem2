/*
Слайд 20
*/

#include <stdio.h>
#include <assert.h>


int power(int base, int n)
{
    assert(n >= 0);

    int result = 1;

    while (n-- > 0)
        result *= base;

    printf("[DBG] power n = %d\n", n);

    return result;
}


int main(void)
{
    int a, n = 5;

    printf("[DBG] main n = %d\n", n);

    a = power(2, n);

    printf("%d^%d = %d\n", 2, n, a);

    return 0;
}
