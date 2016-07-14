/*
Слайд 16
*/

#include <stdio.h>


void f()
{
    printf("f\n");
}


void g(void)
{
    printf("g\n");
}


int main(void)
{
    f();

    g();

    f(1, 2, 3);

//    g(1, 2, 3);

    return 0;
}
