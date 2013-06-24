#include <stdio.h>

int main(int argc, char *argv[])
{
	int c;
	int a=(int)strtoul(argv[1], 0, 0);
	int b=(int)strtoul(argv[2], 0, 0);
	c= a + b;
	printf ("%d\n",c);
	return 0;
}