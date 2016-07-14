/*
Слайд 9
*/

#include <stdio.h>


int max(int a, int b)
{
    if (a < b)
        return b;

    return a;
}


int main(void)
{
    int n_chars;

    max(3, 5);    // странно, но допустимо

    n_chars = printf("Hello, world!\n");
    // после вызова printf n_chars равно 14

    printf("n_chars = %d\n", n_chars);

    (void) printf("Hello, world!\n");
    // явно указано, что возвращаемое значение не используется

    return 0;
}