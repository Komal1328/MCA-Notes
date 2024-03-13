#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void swap(int* a, int* b)
{ 
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int a[], int N, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
 
    if (left < N && a[left] > a[largest])
        largest = left;
    if (right < N && a[right] > a[largest])
        largest = right;
    if (largest != i) 
    {
        swap(&a[i], &a[largest]);
        heapify(a, N, largest);
    }
}

void heapSort(int a[], int N)
{
    for (int i = N / 2 - 1; i >= 0; i--)
        heapify(a, N, i);
    for (int i = N - 1; i >= 0; i--) 
    {
        swap(&a[0], &a[i]);
        heapify(a, i, 0);
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
	heapSort(a,n);
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

