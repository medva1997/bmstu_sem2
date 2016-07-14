/*
Слайд 25
*/

#include <stdio.h>

int main(void)
{
    int a = 1;
    int *p = &a;

    a = 3;

    printf("%d %d\n", a, *p);

    *p = 5;

    printf("%d %d\n", a, *p);

    printf("%p\n", p);

    return 0;
}