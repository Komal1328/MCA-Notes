#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void insertionSort(int a[], int n)
{
    int i, v, j;
    for (i = 1; i < n; i++)
    {
        v = a[i];
        j = i - 1;
        while (j >= 0 && a[j] > v)
        {
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j + 1] = v;
    }
}

void main()
{
	int n,i;
	clock_t start,end,tick;
	printf("Enter the value of n:\t");
	scanf("%d",&n);
	int a[n];
	printf("Enter %d elements\n",n);
	for(i=0;i<n;i++)
	{
		a[i]=(rand()%99+1);
		printf("%d\t",a[i]);
	}
	printf("\n");
	start=clock();
    for(i=0;i<10000;i++)
	insertionSort(a,n);
	end=clock();
	tick=CLOCKS_PER_SEC;
	printf("\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
	}
	printf("\n");
	printf("Start time %ld \n",start);
	printf("end time %ld \n",end);
	double tot_time=(double)(end-start)/(double)tick;
	printf("Total time: %f\n ",tot_time);
	
}


