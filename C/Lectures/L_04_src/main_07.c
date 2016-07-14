/*
Слайд 15
*/

#include <stdio.h>

int main(void)
{
    int sum = 0, i, n = 5;

    // Сумма первых n натуральных чисел
    for (i = 1; i <= n; i++)
        sum += i;

    printf("Total of the first %d numbers is %d\n", n, sum);

    return 0;
}
