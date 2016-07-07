#include <stdio.h>
#include <math.h>

int main(void)
{
	float step,eps,summ,x=0;
	int pos=1;
	float factorial=1;

	printf("Input x, eps\n" );
	scanf("%f%f",&x,&eps);
	float power=x;
	
	step=x;
	summ=x;
	
	while(fabs(step)>eps)
	{	
		factorial=factorial*2*pos*(2*pos+1);
		power=power*x*x;

		step=power/factorial;

		//printf("%f\n", step);

		if(pos%2==1)
			summ=summ-step;
		else
			summ=summ+step;

		pos++;
	}
	printf("summ(x)=%f\n", summ);
	printf("sin(x)=%f\n", sin(x));
	printf("delta=%f\n", fabs(summ-sin(x)));

	
	return 0;

}