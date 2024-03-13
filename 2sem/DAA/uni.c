#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main() {
    int n, i, j, flag, count = 0;
    clock_t start, end, tick;
    int A[n];
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Enter %d elements",n);
    for (i = 0; i < n; i++) 
    {
        scanf("%d\t",&A[i]);
    }
    printf("\n");
    
    for (i = 0; i <=n-2 ; i++) 
    {
        flag = 0;  
        for (j = i+1; j < n-1; j++) 
        {
            if (A[i] == A[j]) 
            {
                flag = 1;  
                break;     
            }
        }
    }
    
    
    if(flag==0)
        printf("Unique");
    else
        printf("not unique");

}

