/*
Слайд 18
*/

#include <stdio.h>

int main(void)
{
    int sum = 0, n = 5;

    for (int i = 1; i <= n; i++)
        sum += i;

    /*
    // error: 'i' undeclared (first use in this function)
    printf("%d\n", i);
    */

    printf("Total of the first %d numbers is %d\n", n, sum);

    return 0;
}
