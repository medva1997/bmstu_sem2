/*
Слайд 22
*/

#include <stdio.h>

int main(void)
{
    int sum, num, i, n = 5;

    // Сложение n положительных чисел

    sum = 0;
    i = 0;
    while (i < n)
    {
        scanf("%d", &num);

        if (n < 0)
            continue;

        sum += num;
        i++;
    }

    printf("Summa of %d positive numbers is %d\n", n, sum);

    return 0;
}