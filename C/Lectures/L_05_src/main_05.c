/*
Слайд 10
*/

#include <stdio.h>


float avg(float a, float b)
{
    float c;

    c = a + b;

    return c / 2.0;
}


void beep(void)
{
    printf("\a");
}


int main(void)
{
    float a, b = -5.0;

    a = avg(2.0, 3.0);

    if (avg(a, b) < 0.0)
        printf("Averadge is negative!\n");

    beep();

    return 0;
}