#include <stdio.h>
#include "functions.h"

#define ERROR_NE -1

/**
 * @brief expected_value - math expected_value
 * @param f[in] - input file
 * @param expectvalue[out] - math expected_value
 * @return 0
 */
int expected_value(FILE *f, float *expectvalue)
{
    float summ=0;
    int n=0;
    float temp;
    while ((fscanf(f, "%f", &temp)) == 1) {
        summ=summ+temp;
        n++;

    }
    if(n==0)
    {
        return ERROR_NE;
    }
    *expectvalue=summ/n;
    return 0;
}



/**
 * @brief dispersionfunc - dispersion
 * @param f[in] - input file
 * @param expectvalue[in] - math expected value
 * @param dispersion[out] - dispersion
 * @return 0
 */

int dispersionfunc(FILE *f,float expectvalue, float *dispersion)
{
    float summ=0;
    int n=0;
    float temp;
    while ((fscanf(f, "%f", &temp)) == 1) {
        summ=summ+(temp-expectvalue)*(temp-expectvalue);
        n++;

    }

    if(n==0)
    {
        return ERROR_NE;
    }

    *dispersion=summ/n;
    return 0;
}
