// C code to implement quicksort

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// Function to swap two elements
void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}
int partition(int a[], int l, int r)
{
	
	int p = a[r];

	
	int i = (l - 1);

	for (int j = l; j <= r - 1; j++) {

		
		if (a[j] < p) {

			
			i++;
			swap(&a[i], &a[j]);
		}
	}
	swap(&a[i + 1], &a[r]);
	return (i + 1);
}

void quickSort(int a[], int l, int r)
{
	if (l < r) {
		int s = partition(a, l, r);
		quickSort(a, l, s - 1);
		quickSort(a, s + 1, r);
	}
}


void main()
{
	int n;
	clock_t start,end;
	printf("Enter the value of n:\t");
	scanf("%d",&n);
	int a[n];
	printf("Enter %d elements\n",n);
	for(int i=0;i<n;i++)
	{
		a[i]=(rand()%99+1);
	}
	printf("\n");
	for(int i=0;i<100000;i++)
	start=clock();
	quickSort(a,0,n-1);
	end=clock();
	printf("\nStart time %ld: \n",start);
	printf("end time %ld: \n",end);
	double tot_time=(double)(end-start)/(double)CLOCKS_PER_SEC;
	printf("Total time: %f\n ",tot_time);
	
}
