/*
Слайд 11
*/

#include <stdio.h>

int main(void)
{
    int sum, i, n = 5;

    // Сумма первых n натуральных чисел
    i = 1;
    sum = 0;
    while (i <= n)
    {
        sum += i;
        i++;
    }

    printf("Total of the first %d numbers is %d\n", n, sum);

    // Сумма первых n натуральных чисел
    i = 1;
    sum = 0;
    while (i <= n)
        sum += i++;

    printf("Total of the first %d numbers is %d\n", n, sum);

    return 0;
}
