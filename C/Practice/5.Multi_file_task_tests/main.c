#include <stdio.h>
#include "functions.h"

#define ERROR_NE -1
#define ERROR_OPEN -2

int main(int argc, char **argv) {
    float expectvalue = 0;
    float dispersion = 0;


     // проверка на существование файла
    FILE *file1 = fopen(argv[1], "r+");
    if (file1 == 0) {
        printf("Не могу открыть файл '%s'", argv[1]);
        return ERROR_OPEN;
    }
    switch(expected_value(file1, &expectvalue))
      {
          case ERROR_NE :
              printf("Недостаточно данных\n");
              fclose(file1);
              return ERROR_NE;
              break;
      }

    rewind(file1);
    switch(dispersionfunc(file1, expectvalue, &dispersion))
      {
          case ERROR_NE :
              printf( "Недостаточно данных");
              fclose(file1);
              return ERROR_NE;
              break;
      }

    fclose(file1);


    printf("\nМатематическое ожидание: %f\n",expectvalue);
    printf("\nДисперсия: %f\n", dispersion);
    return 0;
}
