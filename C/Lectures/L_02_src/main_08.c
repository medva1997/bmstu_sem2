
#include <stdio.h>


/**
 * @brief      [хрень]
 *
 * @param[in]  a     простоа
 * @param[in]  b     { просто б }
 *
 * @return     { description_of_the_return_value }
 */
float avg(float a,float b)
{
	float c;
	c=a+b;
	return c/2.0;
}


/**
 * @brief      { function_description }
 *
 * @return     { description_of_the_return_value }
 */
int main(void)
{
    float tf, tc;

    printf("Enter Celsius temperature: ");
    scanf("%f", &tc);

    tf = (9.0f / 5.0f) * tc + 32.0f;

    printf("Fahrenheit equivalent: %.1f\n", tf);

    return 0;
}