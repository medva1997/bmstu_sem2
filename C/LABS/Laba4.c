#include <stdio.h>
#include <math.h>

int check(int nub);


int main(void)
{
	int read=1;
	int value=0;
	int count=0;

	while(read==1)
	{
		read=scanf("%d",&value);
		if (read==1)
		{
			if (check(value)==0)
			{
				//printf("%d is simple \n",value);
				++count;
			}
			else
			{
				//printf("%d not simple \n",value);
			}
		}
		else
		{
			printf("Number of simple=%d\n",count);
		}
	}

	return 0;
}

int check(int nub)
{ 
	
	if(nub<=0)
	{
		return 1;
	}

	for (int i = 2; i < nub/2+1; ++i)
	{
		if( nub%i==0)
		{
			return 1;
		}	
	}

	return 0;
}