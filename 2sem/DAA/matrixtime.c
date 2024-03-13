#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
void main()
{
	int n=15,i,j,k;
	int a[n][n],b[n][n],c[n][n];
	clock_t start,end,tick;
	printf("Matrix multipication\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			a[i][j]=(rand()%9+1);
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			b[i][j]=(rand()%9+1);
		}
	}
	start=clock();
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			c[i][j]=0;
			for(k=0;k<n;k++)
			{
				c[i][j]=c[i][j]+(a[i][k]*b[k][j]);
			}
		}
	}
	end=clock();
	tick=CLOCKS_PER_SEC;
	
	printf("Multipication is: \n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d\t",c[i][j]);
		}
		printf("\n");
	}
	tick=CLOCKS_PER_SEC;
	printf("The clock tick %ld\n",tick);
	printf("Start time:%ld\n",start);
	printf("End time:%ld\n",end);
    double time_taken = (double)(end-start)/(double)CLOCKS_PER_SEC;
    printf("Time complexity : %f \n",time_taken);
}
