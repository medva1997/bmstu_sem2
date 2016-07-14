#include <stdio.h>

#define OK 0
#define ERROR_NE -1

/**
 * @brief expected_value - math expected_value
 * @param f[in] - input file
 * @param expectvalue[out] - math expected_value
 * @return 0
 */
int expected_value(FILE *f, float *expectvalue)
{
    float summ = 0;
    int n = 0;
    float temp;
    int re = OK;

    while ((fscanf(f, "%f", &temp)) == 1)
    {
        summ = summ + temp;
        n++;

    }
    if (n != 0)
    {
        *expectvalue = summ / n;
    }
    else
        re = ERROR_NE;

    return re;
}


/**
 * @brief dispersionfunc - dispersion
 * @param f[in] - input file
 * @param expectvalue[in] - math expected value
 * @param dispersion[out] - dispersion
 * @return 0
 */

int dispersionfunc(FILE *f, float expectvalue, float *dispersion)
{
    float summ = 0;
    int n = 0;
    float temp;
    int re = OK;

    while ((fscanf(f, "%f", &temp)) == 1)
    {
        summ = summ + (temp - expectvalue) * (temp - expectvalue);
        n++;

    }

    if (n != 0)
    {
        *dispersion = summ / n;

    }
    else
        re = ERROR_NE;

    return re;
}
