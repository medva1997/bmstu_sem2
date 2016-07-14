#include <stdio.h>
#include "functions.h"

#define OK 0
#define ERROR_NE -1
#define ERROR_OPEN -2
#define ERROR_ARG -3

int main(int argc, char **argv)
{
    float expectvalue = 0;
    float dispersion = 0;
    int re = OK;


    // проверка на ввод имени файла
    if (argc < 2)
    {
        re = ERROR_ARG;

    }
    else
    {
        // проверка на существование файла
        FILE *file1 = fopen(argv[1], "r+");
        if (file1 == 0)
        {
            re = ERROR_OPEN;
        }
        else {
            switch (expected_value(file1, &expectvalue))
            {
                case ERROR_NE :
                    re = ERROR_NE;
                    break;
            }
            //Перемешение каретки в начало файла
            rewind(file1);

            switch (dispersionfunc(file1, expectvalue, &dispersion))
            {
                case ERROR_NE :
                    re = ERROR_NE;
                    break;
            }
        }

        if (file1)
            fclose(file1);
    }
    switch (re)
    {
        case ERROR_NE:
            fprintf(stderr, "Недостаточно данных");
            break;
        case ERROR_OPEN:
            fprintf(stderr, "Не могу открыть файл '%s'", argv[1]);
            break;
        case ERROR_ARG:
            fprintf(stderr, "Недостаточно аргументов");
            break;
        case OK:
            printf("\nМатематическое ожидание: %f\n", expectvalue);
            printf("\nДисперсия: %f\n", dispersion);
    }
    return re;
}
