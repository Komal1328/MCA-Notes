#include<stdio.h>
#include<time.h>
#include<stdlib.h>
void main()
{
	int n,i,j,temp;
	clock_t start,end,tick;
	printf("Enter the value of n\n");
	scanf("%d",&n);
	int A[n];
	for(i=0;i<n;i++)
	{
		A[i] = (rand()%900)+1;
		printf("%d\t",A[i]);
	}
	printf("\n");
	
	start = clock();
	for(int x=0;x<1000;x++)
	{
		for(i=0;i<=n-1;i++)
		{
			for(j=0;j<n-1-i;j++)
			{
				if(A[j+1] < A[j])
				{
					temp=A[j];
					A[j]=A[j+1];
					A[j+1]=temp;
				}
			}
		}
	}
	end = clock();
	tick = CLOCKS_PER_SEC;
	printf("The clock tick: %ld\n", tick);
	printf("Start time: %ld\n", start);
	printf("End time: %ld\n", end);    
	double time_taken = (double)(end - start) / (double)tick;
	printf("Time complexity: %f seconds\n", time_taken);		
	for(i=0;i<n;i++)
	{
		printf("%d\t",A[i]);
	}	
}
