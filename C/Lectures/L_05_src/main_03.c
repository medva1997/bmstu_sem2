/*
Слайд 7
*/


float avg(float a, float b)
{
    float c;

    c = a + b;

    return c / 2.0;
}


void try_read_c(void)
{
/*
    // К переменным функции avg из функции try_read_c обращаться нельзя
    // error: 'c' undeclared (first use in this function)
    printf("c is %f\n", c);
*/
}


// Тело функции dummy может быть пустым
void dummy(void)
{
}
