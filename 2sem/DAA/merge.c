#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int p,q,n,i,j,k;;
void merge(int a[], int l, int m, int r)
{
	p = m - l + 1;
	q = r - m;
	int L[p], R[q];
	for(i=0;i<p;i++)
		L[i] = a[l + i];
	for(j=0;j<q;j++)
		R[j] = a[m + 1 + j];	
	i=0;
	j=0;
	k=l;
	while(i<p && j<q) 
	{
		if(L[i]<=R[j]) 
		{
			a[k]=L[i];
			i++;
		}
		else 
		{
			a[k]=R[j];
			j++;
		}
		k++;
	}
	while(i<p) 
	{
		a[k]=L[i];
		i++;
		k++;
	}
	while(j<q) 
	{
		a[k]=R[j];
		j++;
		k++;
	}
}

	
void mergeSort(int a[], int l, int r)
{
	if(l<r) 
	{
		int m = l + (r - l) / 2;
		mergeSort(a, l, m);
		mergeSort(a, m + 1, r);
		merge(a, l, m, r);
	}
}
void main()
{
	
	clock_t start,end,tick;
	printf("Enter the value of n:\t");
	scanf("%d",&n);
	int a[n];
	printf("Enter %d elements\n",n);
	for(i=0;i<n;i++)
	{
		a[i]=(rand()%9+1);
		printf("%d\t",a[i]);
	}
	printf("\n");
	start=clock();
	for(i=0;i<10000;i++)
	mergeSort(a,0,n-1);
	end=clock();
	tick=CLOCKS_PER_SEC;
	printf("\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
	}
	printf("\n");
	printf("Start time %ld: \n",start);
	printf("end time %ld: \n",end);
	double tot_time=(double)(end-start)/(double)tick;
	printf("Total time: %f\n ",tot_time);
	
}


