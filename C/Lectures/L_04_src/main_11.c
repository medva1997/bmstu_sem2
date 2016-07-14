/*
Слайд 20
*/

#include <stdio.h>

int main(void)
{
    int sum, i, n;

    for (sum = 0, i = 1, n = 5; i <= n; sum += i, i++)
        ;

    printf("Total of the first %d numbers is %d\n", n, sum);

    return 0;
}
