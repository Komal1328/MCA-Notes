#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
void main()
{
	int a[100],n=100,i,key,flag=0,pos,j;
	clock_t start,end,tick;
	printf("Linear Search\n");
	for(i=0;i<n;i++)
	{
		a[i]=(rand()%199+1);
	}
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
	}
	printf("Enter key element to be searched\n");
	scanf("%d",&key);
	start=clock();
	for(j=0;j<10000000;j++)
		for(i=0;i<=n;i++)
		{
			if(a[i]==key)
			{
				flag=1;
				pos=i+1;
			}
		}
		end=clock();
		tick=CLOCKS_PER_SEC;
		printf("The clock tick: %ld\n",tick);
		printf("Start time: %ld\n",start);
		printf("End time: %ld\n",end);
		printf("The time was: %ld\n",(end-start)/tick);
		if(flag==0)
			printf("Key element not found\n");
		else
			printf("%d found at position %d\n",key,pos);
}
