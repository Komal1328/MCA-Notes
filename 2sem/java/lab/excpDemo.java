import java.util.*;
class MyException extends Exception
{
	int i,j,n;
	Scanner sc= new Scanner(System.in);
	int a[]=new int[200];
	void input()
	{
		try
		{
			System.out.println("Enter the value of n");
			n=sc.nextInt();
			System.out.println("Enter "+n+" elements");
			for(i=0;i<n;i++)
			{
				a[i]=sc.nextInt();
				for(j=0;j<i;j++)
				{
					if(a[i]==a[j])
					throw new MyException();
				}
			}
		}
		catch(MyException e)
		{
			System.out.println("Caught exception");
			System.out.println("Entered duplicate value");
		}
	}
}
class excpDemo
{
	public static void main(String args[])
	{
		try
		{
			MyException m=new MyException();
			m.input();
		}
		catch(Exception e)
		{
			System.out.println("Error: "+e);
		}
	}
}
