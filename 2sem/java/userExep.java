import java.util.Scanner;
import java.util.*;
class userException extends Exception
{
	int a,b,c;
	Scanner sc=new Scanner(System.in);
	void add()
	{
		try
		{
			System.out.println("Enter value of a:");
			a=sc.nextInt();
			System.out.println("Enter value of b:");
			b=sc.nextInt();
			c=a+b;
			System.out.println("a+b: "+c);
			if(c<0 || c>100)
			{
				throw new userException();
			}
		}
		catch(userException e)
		{
			System.out.println("Cought exception");
			//System.out.println(e.getMessage());
		}
		
	}
}
class userExep
{
	public static void main(String args[])
	{
		try
		{
			userException u=new userException();
			u.add();
		}
		catch(ArithmeticException e)
		{
			System.out.println("Exception");
		}
	}
}


			