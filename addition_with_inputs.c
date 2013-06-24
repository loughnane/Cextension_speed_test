#include <stdio.h>

int main(int argc, char *argv[])//argc is the "argument count", argv is an array of the argument variables
{
	int c; //declare that we will be using a variable c and that it is an integer

	/*three things are happeneing in the two lines below this comment:
	1. the variable (a or b) is being initalized as an integer
	2. the nth argument variable (1st in the case of a, 2nd in the case of b) is being converted to an integer
	3. the newly converted integer is assigned to the variable (a or b)

	note: the 0th argv is generally the name of the function. That is, if you issued the following command:
	$ canconfig can0 start
	then argv[0] is "canconfig", argv[1] is "can0" and argv[2] is "start"
	*/
	int a=(int)strtoul(argv[1], 0, 0);
	int b=(int)strtoul(argv[2], 0, 0);
	c= a + b; //self-explanatory
	return 0; //need to return something at the end of a C function
}