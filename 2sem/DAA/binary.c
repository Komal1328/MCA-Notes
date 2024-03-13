#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int binarySearch(int a[], int l, int r, int k)
{
	l=0;
	r=n-1;
	while (l <= r) 
	{
        	int m = (l+r)/2;
		if (a[m] == k)
            		return m;
        	if (k<a[m])
            		r=m-1;
        	else
            		l=m+1;
    	}
    	return -1;
}
void main(void)
{
    int n,k,r;
    clock_t start,end,tick;
    printf("Enter te value of n\t");
    scanf("%d",&n);
    int a[n];
    printf("Enter %d elements:\n");
    for(int i=0;i<n;i++)
    {
        a[i]=(rand()%99+1);
		printf("%d\t",a[i]);
    }
    printf("\n");
    printf("Enter key element:\t");
    scanf("%d",&k);
	start=clock();
    for(int i=0;i<100;i++)
	 r= binarySearch(a, 0, n - 1, k);
	end=clock();
	tick=CLOCKS_PER_SEC;

	printf("\n");
	if(r==-1)
        printf("Key element not found\n");
    else
        printf("Key element found at position %d \n",r+1);

	printf("Start time %ld: \n",start);
	printf("end time %ld: \n",end);
	double tot_time=(double)(end-start)/(double)tick;
	printf("Total time: %f\n ",tot_time);
   
    
}