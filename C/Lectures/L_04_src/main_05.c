/*
����� 11
*/

#include <stdio.h>

int main(void)
{
    int sum, i, n = 5;

    // ����� ������ n ����������� �����
    i = 1;
    sum = 0;
    while (i <= n)
    {
        sum += i;
        i++;
    }

    printf("Total of the first %d numbers is %d\n", n, sum);

    // ����� ������ n ����������� �����
    i = 1;
    sum = 0;
    while (i <= n)
        sum += i++;

    printf("Total of the first %d numbers is %d\n", n, sum);

    return 0;
}
