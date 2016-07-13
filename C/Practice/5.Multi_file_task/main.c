#include <stdio.h>

#define ERROR_NE -1
#define ERROR_OPEN -2
#define ERROR_ARG -3


int expected_value(FILE *f, float *max_of_identical);
int dispersionfunc(FILE *f,float expectvalue, float *max_of_identical);


int main(int argc, char **argv) {
    float expectvalue = 0;
    float dispersion = 0;

     // проверка на ввод имени файла
    if(argc<1) {
        fprintf(stderr,"Недостаточно аргументов");
        return ERROR_ARG;

    }

     // проверка на существование файла
    FILE *file1 = fopen(argv[1], "r+");
    if (file1 == 0) {
        fprintf(stderr,"Не могу открыть файл '%s'", argv[1]);
        return ERROR_OPEN;
    }
    switch(expected_value(file1, &expectvalue))
      {
          case ERROR_NE :
              fprintf(stderr, "No enough data");
              fclose(file1);
              return -1;
              break;
      }

    rewind(file1);
    switch(dispersionfunc(file1, expectvalue, &dispersion))
      {
          case ERROR_NE :
              fprintf(stderr, "Не достаточно данных");
              fclose(file1);
              return -1;
              break;
      }

    fclose(file1);


    printf("\nМатематическое ожидание: %f\n",expectvalue);
    printf("\nДисперсия: %f\n", dispersion);
    return 0;
}
