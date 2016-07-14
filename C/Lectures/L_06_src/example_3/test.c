#include <stdio.h>
#include "hello.h"
#include "buy.h"

int main(void)
{
	hello();
	printf("If you see hello message, everything is all right.\n");

	goodbuy();
	printf("If you see buy message, everything is all right.\n");

	return 0;
}
