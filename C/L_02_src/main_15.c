#include <stdio.h>

int main(void)
{
  int i;
  float f;

  printf("What are your favorite numbers?\n");
  printf("(Enter an integer and a float.)\n");

  // NB: ������ & ����� ������ ����������!
  scanf("%d%f", &i, &f);

  printf("\nYour favorite numbers are %d and %f!\n", i, f);

  return 0;
}
