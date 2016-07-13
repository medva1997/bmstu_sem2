#include <stdio.h>
#include "functions.h"
#include <math.h>

void rewrite(FILE* file, char* name, char* text)
{
    fopen(name, "w");
    fprintf(file, "%s", text);
    fclose(file);
}

char* filename = "temp.txt";

int main()
{
        float expectvalue=0, dispersion=0;

        int flag = 1;
        FILE* tfile = fopen(filename, "w");
        fclose(tfile);


        tfile = fopen("test1", "r");
        if (expected_value(tfile,&expectvalue) != -1)
            flag = 0;
        fclose(tfile);


        tfile = fopen("test2", "r");
        expected_value(tfile,&expectvalue);
        if( fabs(expectvalue-5.6)>0.000001 )
                flag = 0;
        fclose(tfile);



        tfile = fopen("test3", "r");
        expected_value(tfile,&expectvalue);
        if( fabs(expectvalue-5.5)>0.000001 )
                flag = 0;
         fclose(tfile);




        tfile = fopen("test4", "r");
        expected_value(tfile,&expectvalue);
        if( fabs(expectvalue-3.5)>0.000001  )
                flag = 0;
        fclose(tfile);


        tfile = fopen("test5", "r");
        expected_value(tfile,&expectvalue);
        if( fabs(expectvalue-5.7)>0.0001  )
                flag = 0;
        fclose(tfile);


        if (flag == 1)
            printf("function expected_value passed\n");
        else
            printf("function expected_value NOT passed\n");

        flag=1;

        tfile = fopen("test1", "r");
        int temp=dispersionfunc(tfile,0, &dispersion);
        if (temp!= -1)
            flag = 0;
        fclose(tfile);



        tfile = fopen("test2", "r");
        dispersionfunc(tfile,5.6, &dispersion);
        if( fabs(dispersion-0)>0.0001 )
                flag = 0;
        fclose(tfile);



         tfile = fopen("test3", "r");
        dispersionfunc(tfile,5.5, &dispersion);
        if( fabs(dispersion-0)>0.0001 )
                flag = 0;
        fclose(tfile);



         tfile = fopen("test4", "r");
        dispersionfunc(tfile,3.5, &dispersion);
        if( fabs(dispersion-2.42)>0.0001 )
                flag = 0;
        fclose(tfile);



         tfile = fopen("test5", "r");
        dispersionfunc(tfile,5.7, &dispersion);
        if( fabs(dispersion-5.835)>0.0001 )
                flag = 0;
        fclose(tfile);



        if (flag == 1)
            printf("function  dispersionfunc passed\n");
        else
            printf("function  dispersionfunc NOT passed\n");




}
