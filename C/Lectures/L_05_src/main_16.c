/*
Слайд 29
*/

#include <stdio.h>


int fact_2(int n)
{
    int p;

    for (p = 1; n > 1; n--)
        p *= n;

    return p;
}


int main(void)
{
    int n = 5;

    printf("%d! = %d\n", n, fact_2(n));

    return 0;
}