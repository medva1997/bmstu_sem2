/*
Слайд 26
*/

#include <stdio.h>


void decompose(float f, int *int_part, float *frac_part)
{
    printf("[DBG] decompose %d %f\n", *int_part, *frac_part);

    *int_part  = f;
    *frac_part = f - *int_part;

    printf("[DBG] decompose %d %f\n", *int_part, *frac_part);
}


int main(void)
{
    int i = -5;
    float f = 100.0;

    printf("[DBG] main %d %f\n", i, f);

    decompose(3.14159, &i, &f);

    printf("[DBG] main %d %f\n", i, f);

    return 0;
}
