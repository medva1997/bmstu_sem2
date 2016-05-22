#include <stdio.h>

int main(void)
{
    float tf, tc;

    printf("Enter Celsius temperature: ");
    scanf("%f", &tc);

    tf = (9.0f / 5.0f) * tc + 32.0f;

    printf("Fahrenheit equivalent: %.1f\n", tf);

    return 0;
}