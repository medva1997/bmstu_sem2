/*
Слайд 9
*/

#include <stdio.h>

int main(void)
{
    int mark = 4;

    switch (mark)
    {
        case 5:  printf("Excellent\n");
        case 4:  printf("Good\n");
        case 3:  printf("Averadge\n");
        case 2:  printf("Poor\n");
        default: printf("Illegal mark\n");
    }

    return 0;
}