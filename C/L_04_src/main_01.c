/*
Слайд 3
*/

#include <stdio.h>

int main(void)
{
    int x = 5, y = 10, max = x > y ? x : y;

    printf("Max of %d and %d is %d\n", x, y, max);

    // Можно обойтись без переменной max
    printf("Max of %d and %d is %d\n", x, y, x > y ? x : y);

    return 0;
}