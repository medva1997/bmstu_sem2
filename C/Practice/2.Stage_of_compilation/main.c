//первые 10 чисел фибоначи отличные от 1 1
#include <stdio.h>
#define COUNT 10


int work=1;
int myarray[]={1,2,3,4};
void print(int for_print)
{
	printf("%d\n",for_print );
}

int main(void)
{
	int first=1,second=1;

	//вычисляем COUNT чисел
	for (int i = 0; i < COUNT; ++i)
	{
		first=first+second;
		second=first-second;
		print(first);
	}
	return 0;
}
