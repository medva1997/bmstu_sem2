/*
Слайд 4
*/

#include <stdio.h>

int main(void)
{
    int mark = 4;

    if (mark == 5)
        printf("Excellent\n");
    else if (mark == 4)
        printf("Good\n");
    else if (mark == 3)
        printf("Averadge\n");
    else if (mark == 2)
        printf ("Poor\n");
    else
        printf("Illegal mark\n");

    switch (mark)
    {
        case 5:  printf("Excellent\n");
                 break;
        case 4:  printf("Good\n");
                 break;
        case 3:  printf("Averadge\n");
                 break;
        case 2:  printf("Poor\n");
                 break;
        default: printf("Illegal mark\n");
                 break;
    }

    return 0;
}