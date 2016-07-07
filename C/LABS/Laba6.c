#include <stdio.h>
#include <math.h>

void large_of(float *x, float *y)
{
	if(*x>*y)
	{
		*y=*x;
	}
	else
	{
		*x=*y;
	}
}

int main(void)
{	
	float x,y;

	printf("Input x, y\n" );
	if(scanf("%f%f",&x,&y)!=2)
	{
		printf("Nothing to do. Exit.\n");
		return 1;
	}
	else
	{
		large_of(&x,&y);
		printf("x=%f y=%f \n",x,y);

	}
}