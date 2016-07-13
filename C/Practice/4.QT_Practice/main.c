#include <stdio.h>
int main(void)
{
    int max = 0, count = 1,num;
    scanf("%d", &max);
    while (scanf("%d", &num) == 1)
    {
        if (num > max)
        {
            max = num;
            count=1;
        }
        else
            if (num == max)
                count++;
    }
    printf("max %d, count %d\n", max, count);
    return 0;
}
