#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main() {
    int n, i, j, flag, count = 0;
    clock_t start, end, tick;
    int A[n];
    printf("Enter the value of n: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) 
    {
        A[i] = (rand() % 900) + 1;
        printf("%d\t",A[i]);
    }
    printf("\n");
    start = clock();
    
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
    
    end = clock();
    
    printf("Number of Unique Elements: %d\n", count);

    tick = CLOCKS_PER_SEC;
    printf("The clock tick: %ld\n", tick);
    printf("Start time: %ld\n", start);
    printf("End time: %ld\n", end);
    double time_taken = (double)(end - start) / (double)CLOCKS_PER_SEC;
    printf("Time complexity: %f seconds\n", time_taken);

    return 0;
}

