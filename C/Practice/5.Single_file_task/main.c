#include <stdio.h>

#define OK 0
#define READ_ERR -1

/**
 * @brief process - The largest number of contiguous
 * @param f[in] - input file
 * @param max_of_identical[out] - number of contiguous
 * @return 0
 */

int process(FILE *f, int *max_of_identical);

int main(void)
{
    int max_of_identical = 0;

    int flag = process(stdin, &max_of_identical);

    switch (flag)
    {
        case (-1) :
            fprintf(stderr, "BAD INPUT");
            break;
        case 0 :
            printf("\nНаибольшее число подряд идущих: %d\n", max_of_identical);
            break;
    }

    return OK;
}

//находит наибольшее число подряд идущих элементов последовательности, которые равны друг другу;
int process(FILE *f, int *max_of_identical)
{
    int current_element = 0;
    int element_before = 0;
    int max_length_of_identical = 1;
    int temp_max_length_of_identical = 1;
    int re=OK;//for return


    if ((fscanf(f, "%d", &current_element)) == 1)// -1 нет данныых для ввода
    {
        element_before = current_element;
    }
    else
    {
        re=READ_ERR;
    }


    while (((fscanf(f, "%d", &current_element)) == 1)&&(re == 0))
    {

        if (current_element == element_before) {
            temp_max_length_of_identical++;
        }
        else {
            temp_max_length_of_identical = 1;
        }

        if (temp_max_length_of_identical > max_length_of_identical) {
            max_length_of_identical = temp_max_length_of_identical;
        }

        element_before = current_element;

    }
    *max_of_identical = max_length_of_identical;

    return re;
}
