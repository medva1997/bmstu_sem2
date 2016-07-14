/*
Слайд 13
*/

#include <stdio.h>


int main(void)
{
    float a = avg(2.0, 3.0);

    printf("%f\n", a);

    return 0;
}


float avg(float a, float b)
{
    return (a + b) / 2.0;
}
