/*
����� 9
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

    max(3, 5);    // �������, �� ���������

    n_chars = printf("Hello, world!\n");
    // ����� ������ printf n_chars ����� 14

    printf("n_chars = %d\n", n_chars);

    (void) printf("Hello, world!\n");
    // ���� �������, ��� ������������ �������� �� ������������

    return 0;
}