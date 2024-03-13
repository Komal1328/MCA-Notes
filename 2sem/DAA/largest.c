#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

int main() 
{
    int n, i;
    clock_t start,end,tick;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d numbers:\n", n);
    for (i = 0; i < n; i++) 
    {
        a[i]=(rand()%900+1);
        printf("%d\t",a[i]);
    }
    printf("\n");
    start=clock();
    int maxval = a[0];
    for(int j=0; j<100000 ;j++)
    {
        for (i = 1; i < n; i++) 
        {
            if (a[i] > maxval)
            {
                maxval = a[i];
            }
        }
    }
    end=clock();
    printf("The largest number is: %d\n", maxval);
	tick=CLOCKS_PER_SEC;
	printf("The clock tick %ld\n",tick);
	printf("Start time:%ld\n",start);
	printf("End time:%ld\n",end);
    double time_taken = (double)(end-start)/(double)tick;
    printf("Time complexity : %f \n",time_taken);
    return 0;
}

