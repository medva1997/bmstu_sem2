#include <stdio.h>

int main(void)
{
    int width, length;
    float speed;

    width = 5;
    length = 4;

    speed = 25.34f;

    printf("Width: %d\n", width);

    printf("Speed: %f\n", speed);

    printf("Width: %d, Length: %d\n", width, length);

    return 0;
}