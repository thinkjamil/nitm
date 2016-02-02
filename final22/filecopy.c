#include<stdio.h>

int main ( int argc, char *argv[] )
{
	FILE *src, *dest;
	char text;
	src = fopen(argv[1], "r");
	if (src == NULL) 
	{
		printf("cannot open this file");
		return 1;
	}
	dest = fopen(argv[2], "w");
	if (dest == NULL) 
	{
		puts("Not able to open this file");
		fclose(src);
		return 1;
	}
	do
	{
		text = fgetc(src);
		fputc(text, dest);
	}while(text != EOF);
	fcloseall();
	return 0;
}
