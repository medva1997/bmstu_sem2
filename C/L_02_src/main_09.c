#include <stdio.h>

#define SCALE_FACTOR    (9.0f / 5.0f)
#define FREEZING_PT     32.0f

int main(void)
{
    float tf, tc;

    printf("Enter Celsius temperature: ");
    scanf("%f", &tc);

    tf = SCALE_FACTOR * tc + FREEZING_PT;

    printf("Fahrenheit equivalent: %.1f\n", tf);

    return 0;
}