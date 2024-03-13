#include<stdio.h>
#include <stdlib.h>
#include <time.h>
int fact(int n)
{
	if(n==0)
		return 1;
	else
		return n*fact(n-1);
}
void main()
{
	int n,factn;
	clock_t start, end, tick;
	printf("Enter the value of n:\n");
	scanf("%d",&n);
	start = clock();
	factn = fact(n);
	end = clock();
	printf("Facotorial of %d is: %d\n",n,factn);
	
	tick = CLOCKS_PER_SEC;
	printf("The clock tick: %ld\n", tick);
	printf("Start time: %ld\n", start);
	printf("End time: %ld\n", end);
	double time_taken = (double)(end - start) / (double)tick;
	printf("Time complexity: %f seconds\n", time_taken);
}
