#include <stdio.h>
#include <math.h>



int main(void)
{
	float a,b,c,d,x1,x2=0;
	int read=0;
	printf("Input a,b,c\n" );
	read=scanf("%f%f%f",&a,&b,&c);

	if( read!=3)
	{
		printf("Error Input\n");
		return 0;		
	}

	printf("a=%f\nb=%f\nc=%f\n",a,b,c );
	if(a!=0)
	{
		d=b*b-4*a*c;
		if(d<0)
		{
			printf("Real roots not found");
		}
		else if(d==0)
		{
			x1=-b/(2*a);
			printf("Only one root: %5.4f",x1);

		}
		else if(d>0)
		{
			x1=(-b+sqrt(d))/(2*a);
			x2=(-b-sqrt(d))/(2*a);
			printf("Two roots : \n%5.4f\n%5.4f",x1,x2);

		}


	}
	else
		if(b!=0)
		{
			x1=-c/b;
			printf("Root: %5.4f",x1);
			
		}
		else if (c==0)
		{
			printf("Root can be any");
		}
		else
		{
			printf("Not correct input");

		}
		return 0;

}
