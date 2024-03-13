#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
void main() 
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
    int maxval = a[0];
    {
        for (i = 1; i < n; i++) 
        {
            if (a[i] > maxval) 
            {
                maxval = a[i];
            }
        }
    }
    printf("The largest number is: %d\n", maxval);
	
}

