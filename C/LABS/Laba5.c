#include <stdio.h>
#include <math.h>

void swap(int *x, int *y)
{
	*x=*x+*y;
	*y=*x-*y;
	*x=*x-*y;
}


int main(void)
{	
	int x,y;

	printf("Input X, Y\n" );
	if(scanf("%d%d",&x,&y)!=2)
	{
		printf("Nothing to do. Exit.\n");
		return 1;
	}
	else
	{
		swap(&x,&y);
		printf("x=%d y=%d \n",x,y);

	}
}