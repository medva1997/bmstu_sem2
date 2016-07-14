/*
Слайд 27
*/

#include <stdio.h>


int fact(int n)
{
    if (n == 0)
        return 1;

    return n * fact(n - 1);
}


int main(void)
{
    int n = 5;

    printf("%d! = %d\n", n, fact(n));

    return 0;
}