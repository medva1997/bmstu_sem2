/*
Слайд 7
*/

#include <stdio.h>

int main(void)
{
    int mark = 4;

    switch (mark)
    {
        case 5:  
        case 4:  
        case 3:  printf("Passing\n");
                 break;
        case 2:  printf("Failing\n");
                 break;
        default: printf("Illegal mark\n");
                 break;
    }

    return 0;
}