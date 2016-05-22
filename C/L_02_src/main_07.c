#include <stdio.h>

int main(void)
{
    int width, length, area;

    printf("Enter width of rectangle: ");
    scanf("%d", &width);
    printf("Enter length of rectangle: ");
    scanf("%d", &length);

    area = width * length;

    printf("Area of rectangl: %d\n", area);

    return 0;
}