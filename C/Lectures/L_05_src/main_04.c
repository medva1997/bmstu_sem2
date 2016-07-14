/*
Слайд 9
*/

#include <stdio.h>


int max(int a, int b)
{
    if (a < b)
        return b;

    return a;
}


void print_pos(int a)
{
    if (a < 0)
        return;

    printf("%d\n", a);
}


void beep(void)
{
    printf("\a");

    // обычно не пишут
    return;
}
