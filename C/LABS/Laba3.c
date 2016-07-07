#include <stdio.h>
#include <math.h>

int main(void)
{	
	
	int value=0;
	int maxvalue=0;
	int counter=0;

	
	if(scanf("%d",&value)!=1)
	{
		printf("Nothing to do. Exit.\n");
		return 1;
	}
	else
	{
		maxvalue=value;
		counter=1;
	}

	while(scanf("%d",&value)==1)
	{
			
		if(value>maxvalue)
		{
			maxvalue=value;
			counter=0;
		}
		if(value==maxvalue)
			++counter;
	}
	
		printf("Max=%d founded %d times \n",maxvalue,counter);
	return 0;
}