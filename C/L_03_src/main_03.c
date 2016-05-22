#include <stdio.h>

int main(void)
{
	int i = 1;

	printf("i is %d\n", ++i);
	printf("i is %d\n", i);

	i = 1;
	printf("i is %d\n", i++);
	printf("i is %d\n", i);

    return 0;
}