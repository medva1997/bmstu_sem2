#include <stdio.h>

int main(void)
{
    int i = 157;
    float f = 3.14;

    // Первый аргумент - строка-форматирования. Она может
    // содержать спецификаторы (%d, %f) и esc-последовательности
    // (\n).
    printf("My favorite numbers are %d and %f\n", i, f);

    printf("%f %e %g\n", 7.123, 7.123, 7.123);


    return 0;
}
