/*
Слайд 16
*/

#include <stdio.h>

int main(void)
{
    int sum = 0, i, n = 5;

    i = 0;
    for ( ; i <= n; )
        sum += i++;

    printf("Total of the first %d numbers is %d\n", n, sum);

    return 0;
}
